# Smart AI Support Assistant

## About the Project

This project was developed as my final capstone project during my AI internship at Sohail Smart Solutions.

The assistant can answer questions about the company, retrieve live weather information, and perform basic mathematical calculations. It also includes error handling and input validation to make the system more reliable.

## Features

- Company knowledge base
- Live weather information using the Open-Meteo API
- Basic calculator
- AI-generated responses using the Gemini API
- Error handling and input validation

## Technologies Used

- Python
- Google Gemini API
- Open-Meteo API
- Requests
- GitHub

## Project Structure

- **main.py** – Runs the AI assistant.
- **knowledge_base.py** – Stores company information.
- **tools.py** – Contains the weather and calculator tools.
- **requirements.txt** – Lists the required Python libraries.
- **.gitignore** – Excludes unnecessary files.
- **README.md** – Project documentation.

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/vxflame/Smart-AI-Support-Assistant.git
```

2. Open the project folder.

```bash
cd Smart-AI-Support-Last
```

3. Install the required libraries.

```bash
pip install -r requirements.txt
```

4. Set your Gemini API key as an environment variable named `GEMINI_API_KEY`.

5. Run the project.

```bash
python main.py
```

## Example Questions

- What services does Sohail Smart Solutions provide?
- What is the weather in Dubai?
- 35 * 18

## Current Limitations

- The knowledge base is limited.
- Internet is required for the weather feature.
- A Gemini API key is required.
- The project runs in the terminal.

## Future Improvements

- Expand the knowledge base.
- Add more APIs.
- Add conversation memory.
- Build a web interface.

## Author

**Abdelrahaman mohamed**

AI Intern – Sohail Smart Solutions
