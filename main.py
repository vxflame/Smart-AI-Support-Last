import os
import re

from google import genai

from knowledge_base import retrieve_information
from tools import calculator, weather_tool


def get_gemini_client():
    """Create the Gemini client using an environment variable."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    return genai.Client(api_key=api_key)


def looks_like_calculation(text: str) -> bool:
    """Check whether the input looks like a basic calculation."""

    allowed_pattern = r"^[0-9+\-*/().%\s]+$"
    return bool(re.fullmatch(allowed_pattern, text.strip()))


def extract_city(question: str) -> str | None:
    """Extract a city name from a simple weather question."""

    patterns = [
        r"weather in (.+)",
        r"temperature in (.+)",
        r"weather for (.+)",
    ]

    lower_question = question.lower().strip()

    for pattern in patterns:
        match = re.search(pattern, lower_question)

        if match:
            return match.group(1).strip(" ?.")

    return None


def generate_ai_response(question: str, context: str | None = None) -> str:
    """Generate a simple response using Gemini."""

    client = get_gemini_client()

    if client is None:
        if context:
            return context

        return (
            "I could not find an answer in the available tools or knowledge base. "
            "The Gemini API key is also not configured."
        )

    prompt = (
        "You are a simple support assistant for Sohail Smart Solutions. "
        "Answer clearly, briefly, and professionally."
    )

    if context:
        prompt += f"\nUse this information when answering:\n{context}"

    prompt += f"\nUser question: {question}"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text.strip()

        return "I could not generate a response."

    except Exception:
        if context:
            return context

        return "The AI service is not available right now."


def support_agent(question: str) -> str:
    """Route the user's question to the correct tool or knowledge source."""

    question = question.strip()

    if not question:
        return "Please enter a question."

    if looks_like_calculation(question):
        return calculator(question)

    if "weather" in question.lower() or "temperature" in question.lower():
        city = extract_city(question)

        if city:
            return weather_tool(city)

        return "Please ask using a city name, for example: What is the weather in Dubai?"

    information = retrieve_information(question)

    if information:
        return generate_ai_response(question, information)

    return generate_ai_response(question)


def main():
    print("Smart AI Support Assistant")
    print("Type 'exit' to stop the program.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break

        response = support_agent(user_input)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
