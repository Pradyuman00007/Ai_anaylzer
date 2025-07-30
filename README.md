# Trade Opportunities API 🚀

A FastAPI-based microservice that analyzes sector-wise trade opportunities in India using Google's Gemini 2.5 Pro API and web scraping. Outputs are returned in structured Markdown format.

---

## 🧠 Features

- 🔍 Sector analysis using generative AI (Gemini 2.5 Pro)
- 🌐 Web scraping of live market data (optional enhancement)
- 📝 Markdown-formatted output for easy reporting
- 🗃️ In-memory architecture (no database required)
- ☁️ Easily deployable and version-controlled via Git

---

## ⚙️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- [Google Generative AI](https://ai.google.dev/)
- `dotenv` for environment variable loading

---

## 🧪 Setup & Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/trade-opportunities-api.git
cd trade-opportunities-api
2. Create project folder and virtual environment

mkdir Ai_analyzer
cd Ai_analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Create app folder and place Python files inside it
Inside Ai_analyzer, create the structure:


Ai_analyzer/
├── venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── ai_analysis.py
│   ├── collector.py
│   ├── markdown_reporter.py
├── .env
├── .gitignore
└── README.md
4. Install dependencies
If you don’t have a requirements.txt, run:


pip install fastapi uvicorn python-dotenv google-generativeai
To freeze the requirements:

bash
Copy
Edit
pip freeze > requirements.txt
🔐 Environment Variables
Create a .env file in the Ai_analyzer/ root:

ini

GEMINI_API_KEY=your_google_gemini_api_key_here
🚀 Running the Server
Run the FastAPI server:


cd app
uvicorn main:app --reload
Access the API at:

arduino
Copy
Edit
http://127.0.0.1:8000/analyze/<sector>
Example:


http://127.0.0.1:8000/analyze/pharmaceutical
🧠 Gemini API Usage
We use google.generativeai with the Gemini model.


import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")
Update to Gemini 2.5 Pro if available:

model = genai.GenerativeModel("gemini-2.5-pro-latest")
📁 Project Structure
Ai_analyzer/
├── venv/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── ai_analysis.py
│ ├── collector.py
│ ├── markdown_reporter.py
├── .env
├── .gitignore
└── README.md
