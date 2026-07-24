import ast
import operator
import requests


def weather_tool(city: str) -> str:
    """Return the current weather for a city using Open-Meteo."""

    city = city.strip()

    if not city:
        return "Please enter a city name."

    try:
        location_url = "https://geocoding-api.open-meteo.com/v1/search"

        location_response = requests.get(
            location_url,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=10,
        )
        location_response.raise_for_status()

        location_data = location_response.json()
        results = location_data.get("results")

        if not results:
            return f"I could not find weather information for {city}."

        location = results[0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m",
                "timezone": "auto",
            },
            timeout=10,
        )
        weather_response.raise_for_status()

        weather_data = weather_response.json()
        current = weather_data.get("current", {})

        temperature = current.get("temperature_2m")
        wind_speed = current.get("wind_speed_10m")

        if temperature is None:
            return "The weather service returned incomplete information."

        place = f"{city_name}, {country}" if country else city_name

        return (
            f"The current temperature in {place} is {temperature}°C "
            f"with a wind speed of {wind_speed} km/h."
        )

    except requests.RequestException:
        return "The weather service is not available right now."

    except (KeyError, TypeError, ValueError):
        return "There was a problem reading the weather information."


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _evaluate_expression(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _evaluate_expression(node.left)
        right = _evaluate_expression(node.right)
        return _ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        value = _evaluate_expression(node.operand)
        return _ALLOWED_OPERATORS[type(node.op)](value)

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Safely calculate a basic mathematical expression."""

    expression = expression.strip()

    if not expression:
        return "Please enter a calculation."

    try:
        parsed = ast.parse(expression, mode="eval")
        result = _evaluate_expression(parsed.body)
        return f"The answer is {result}."

    except ZeroDivisionError:
        return "A number cannot be divided by zero."

    except (SyntaxError, ValueError, TypeError):
        return "Please enter a valid mathematical expression."
