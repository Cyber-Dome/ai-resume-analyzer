# AI Resume Analyzer

A simple Python Tkinter desktop app that analyzes resume PDFs and gives:
- ATS score
- job-role match percentage
- optional AI feedback using OpenRouter

## Features
- Upload PDF resume
- Extract text using PyPDF2
- Calculate basic ATS score
- Compare resume with selected job role skills
- Get AI suggestions for improvements

## Tech Stack
- Python
- Tkinter
- Requests
- PyPDF2
- OpenRouter API

## Project Structure
```
ai_resume_analyzer/
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` values into your environment
4. Run:
   ```bash
   python main.py
   ```

## Environment Variables
Set these before running:
- `OPENROUTER_API_KEY`
- `OPENROUTER_MODEL` (optional)

## Supported Roles
- python developer
- web developer
- data analyst



## Author
Amal Aji
- Blog: https://domebytes.blogspot.com
- GitHub: https://github.com/Cyber-Dome
- LinkedIn: https://www.linkedin.com/in/amal-aji-0a294932b
