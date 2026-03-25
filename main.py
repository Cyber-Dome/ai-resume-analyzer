import os
import tkinter as tk
from tkinter import filedialog, messagebox

import requests
import PyPDF2

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3-8b-instruct")

JOB_SKILLS = {
    "python developer": ["python", "django", "flask", "api", "sql"],
    "web developer": ["html", "css", "javascript", "react"],
    "data analyst": ["python", "excel", "sql", "pandas"],
}


def read_pdf(file_path: str) -> str:
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as exc:
        messagebox.showerror("Error", f"Failed to read PDF: {exc}")
    return text



def calculate_ats_score(text: str) -> int:
    text = text.lower()
    score = 0

    if len(text) > 300:
        score += 20
    if "python" in text:
        score += 15
    if "project" in text:
        score += 10
    if "experience" in text:
        score += 15
    if "skill" in text:
        score += 10

    return min(score, 100)



def calculate_job_match(text: str, job_role: str) -> int:
    text = text.lower()
    job_role = job_role.lower().strip()

    if job_role not in JOB_SKILLS:
        return 0

    required_skills = JOB_SKILLS[job_role]
    matched = sum(1 for skill in required_skills if skill in text)
    return int((matched / len(required_skills)) * 100)



def analyze_with_ai(text: str, job_role: str) -> str:
    if not API_KEY:
        return (
            "AI analysis skipped. Add your OpenRouter key in an environment variable named "
            "OPENROUTER_API_KEY to enable AI feedback."
        )

    prompt = f"""
You are an expert resume analyzer.

Analyze this resume for a {job_role} role.

Give:
- Strengths
- Weaknesses
- Missing skills
- Improvements

Resume:
{text[:1500]}
"""

    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )

        if response.status_code != 200:
            return f"API Error {response.status_code}:\n{response.text}"

        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", str(result))
    except Exception as exc:
        return f"Error: {exc}"



def analyze_resume(text: str, job_role: str) -> str:
    if not text.strip():
        return "No text found in PDF!"

    ats_score = calculate_ats_score(text)
    job_match = calculate_job_match(text, job_role)
    ai_text = analyze_with_ai(text, job_role)

    return f"""
===============================
ATS Score: {ats_score}/100
Job Match: {job_match}%
===============================

{ai_text}
"""



def upload_pdf() -> None:
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    job_role = job_entry.get().strip()
    if not job_role:
        messagebox.showerror("Error", "Enter job role!")
        return

    resume_text = read_pdf(file_path)
    result = analyze_resume(resume_text, job_role)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


window = tk.Tk()
window.title("AI Resume Analyzer")
window.geometry("750x600")


tk.Label(window, text="AI Resume Analyzer", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(window, text="Enter Job Role (e.g., python developer)").pack()
job_entry = tk.Entry(window, width=40)
job_entry.pack(pady=5)

tk.Button(window, text="Upload Resume (PDF)", command=upload_pdf).pack(pady=10)

output_text = tk.Text(window, wrap="word")
output_text.pack(expand=True, fill="both", padx=10, pady=10)

window.mainloop()
