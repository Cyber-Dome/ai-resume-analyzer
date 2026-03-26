# 🚀 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Stars](https://img.shields.io/github/stars/Cyber-Dome/ai-resume-analyzer?style=social)

---

## 🎥 Project Demo

<p align="center">
  <a href="https://youtu.be/oarjAtPs4-k">
    <img src="https://img.youtube.com/vi/oarjAtPs4-k/maxresdefault.jpg" width="700" alt="AI Resume Analyzer Demo"/>
  </a>
</p>

<p align="center">
  ▶️ <b>Click the image to watch the full demo video</b>
</p>

👉 Watch how the app analyzes resumes, calculates ATS score, and provides AI feedback in real-time.

---

## 📌 About the Project

AI Resume Analyzer is a Python-based desktop application built using Tkinter.

It allows users to upload their resume (PDF) and get:

- 📊 ATS Score  
- 🎯 Job-role match percentage  
- 🤖 AI-based suggestions (strengths, weaknesses, improvements)  

This project demonstrates real-world concepts like PDF parsing, keyword analysis, and AI integration.

---

## ✨ Features

- 📄 Upload PDF resume  
- 🔍 Extract text using PyPDF2  
- 📊 Calculate ATS score  
- 🎯 Match resume with job roles  
- 🤖 AI-powered feedback using OpenRouter  
- 🖥️ Clean GUI using Tkinter  

---

## 🛠️ Tech Stack

- Python 🐍  
- Tkinter  
- Requests  
- PyPDF2  
- OpenRouter API  

---

## 📁 Project Structure

ai_resume_analyzer/
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

---

## ⚙️ Setup & Installation

1️⃣ Clone the repository

git clone https://github.com/Cyber-Dome/ai-resume-analyzer.git  
cd ai_resume_analyzer  

---

2️⃣ Install dependencies

pip install -r requirements.txt  

---

3️⃣ Setup environment variables

Create a `.env` file and add:

OPENROUTER_API_KEY=your_api_key_here  
OPENROUTER_MODEL=meta-llama/llama-3-8b-instruct  

---

4️⃣ Run the application

python main.py  

---

## 🧠 Supported Job Roles

- Python Developer  
- Web Developer  
- Data Analyst  

---

## 📸 Output Example

The application provides:

- ATS Score (out of 100)  
- Job Match Percentage  
- AI-generated resume feedback  

---

## ⚠️ Disclaimer

This project is built for educational purposes.

The ATS scoring system is a basic implementation and does not represent real-world enterprise ATS systems.

---

## 🔗 Connect with Me

Blog: https://domebytes.blogspot.com  
GitHub: https://github.com/Cyber-Dome  
LinkedIn: https://www.linkedin.com/in/amal-aji-0a294932b  
YouTube: https://www.youtube.com/@cyberdomeee  

---

## ⭐ Support

If you found this project useful:

- Star this repository  
- Fork it  
- Share with others  

---

## 🚀 Future Improvements

- Convert to web app (Django/Flask)  
- Add more job roles  
- Improve ATS scoring logic  
- Resume comparison feature  
- Export analysis report  
