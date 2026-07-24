# Smart AI Support Assistant

## About the Project

This project was developed as my final capstone project during my AI internship at Sohail Smart Solutions.

The assistant can answer basic questions about the company, provide live weather information, and solve mathematical calculations. It also includes input validation and error handling to make the program more reliable.

## Features

- Answers questions from a small company knowledge base
- Provides live weather information
- Solves basic mathematical calculations
- Uses the Gemini API for natural responses
- Handles empty or invalid input
- Returns clear messages when an API is unavailable

## Technologies Used

- Python
- Google Gemini API
- Open-Meteo API
- Requests
- GitHub

## Project Files

The project is divided into a few simple files.

- **main.py** runs the assistant and connects all parts of the project.
- **knowledge_base.py** stores the company information.
- **tools.py** contains the weather and calculator functions.
- **requirements.txt** lists the required Python libraries.
- **.gitignore** prevents private or unnecessary files from being uploaded.

## How to Run

1. Download or clone the repository.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Smart-AI-Support-Last.git
```

2. Open the project folder.

```bash
cd Smart-AI-Support-Last
```

3. Install the required libraries.

```bash
pip install -r requirements.txt
```

4. Add your Gemini API key as an environment variable named:

```text
GEMINI_API_KEY
```

5. Run the project.

```bash
python main.py
```

## Example Questions

```text
What services does Sohail Smart Solutions provide?
```

```text
What is the weather in Dubai?
```

```text
35 * 18
```

## Limitations

- The company knowledge base is small.
- Internet access is required for the weather tool and Gemini API.
- A valid Gemini API key is required for AI-generated answers.
- The project currently runs in the terminal.

## Future Improvements

- Add more company information
- Add more external tools and APIs
- Add conversation memory
- Build a web interface
- Improve the retrieval system

## Author

**Abdelrahaman Mohamed**

AI Intern – Sohail Smart Solutions
