[//]: # (# Multi-Agent Intelligent Learning & Coding Assistant)
# 💡 Multi-Agent Learning & Coding Assistant
### *Built by **- Keval Ramoliya***  


A powerful multi-agent system built with Python, Flask, MySQL, and Google Gemini.

This system provides AI-powered capabilities for learning, coding, project planning, research, document analysis, and code review — all in one unified platform.

---

## 🚀 Overview

This project implements a full **multi-agent architecture** with intelligent routing and modular capabilities.  
Each agent specializes in one domain, ensuring accurate, structured, and helpful output.

### 🔥 Included Agents:
1. 🧠 Coding Problem Solver Agent  
2. 📚 Topic Learning Agent  
3. 🧱 Project Builder Agent  
4. 🛠 Code Review Agent  
5. 🔍 Research Agent  
6. 📄 Document Reader Agent (PDF/Text)

---

## ✨ Features

### 🧠 Coding Problem Solver Agent
- Code explanation  
- Debugging  
- Optimization  
- Test-case generator  
- Complexity analysis  

### 📚 Topic Learning Agent
- Teaches DSA, SQL, ML, Python  
- Generates notes & mind maps  
- Creates quizzes  
- Tracks learning using sessions  

### 🧱 Project Builder Agent
- Generates folder structures  
- ER diagrams  
- API documentation  
- Model & controller stubs  
- Step-by-step project plan  
- Test plan  

### 🛠 Code Review Agent
- Deep code inspection  
- Line-by-line review  
- Bug detection  
- Refactoring suggestions  
- Security vulnerabilities  
- Time/space complexity  

### 🔍 Research Agent
- Finds best tutorials online  
- GitHub repo recommendations  
- StackOverflow-style answers  
- Summaries & roadmaps  

### 📄 Document Reader Agent (PDF/Text)
- PDF text extraction  
- Document summarization  
- Key notes generation  
- Quiz creation  
- Glossary extraction  

---

## 🧱 Tech Stack

### Backend
- Python  
- Flask  
- MySQL  
- SQLAlchemy  
- Google Gemini API  
- PyPDF2  

### Frontend
- HTML  
- CSS  
- JavaScript  
- marked.js for Markdown rendering  

### Other Tools
- flask-cors  
- dotenv  
- JSON file logging  

---

## 📂 Folder Structure

```
multi_agent_learning_assistant/
│
├── backend/
│   ├── agents/
│   │   ├── coding_agent/
│   │   ├── learning_agent/
│   │   ├── project_builder_agent/
│   │   ├── code_review_agent/
│   │   ├── research_agent/
│   │   ├── document_reader_agent/
│   │
│   ├── routes/
│   │   ├── chat_routes.py
│   │   ├── code_review_routes.py
│   │   ├── research_routes.py
│   │   ├── document_routes.py
│   │
│   ├── utils/logger.py
│   ├── config/
│   ├── database/
│   ├── app.py
│
├── frontend/
│   ├── index.html
│   ├── chat.css
│   ├── chat.js
│
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-learning-assistant.git
cd multi-agent-learning-assistant
```

---

## 2️⃣ Create Virtual Environment

### Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Environment Variables

Create a `.env` file inside the `backend/` folder:

```
GENAI_API_KEY=YOUR_KEY_HERE
DATABASE_URL=mysql+pymysql://username:password@localhost/YOUR_DATABASE_NAME

FLASK_ENV=development

DB_USER=root
DB_PASS=YOUR_PASSWORD
DB_HOST=localhost
DB_NAME=YOUR_DATABASE_NAME


```

---

## 5️⃣ Initialize MySQL Database

Update `settings.py`, then run:

```bash
python -m backend.database.db
```

---

## 🖥 Running the Project

### Backend:
```bash
cd backend
python  -m backend.app
```

Runs at:
```
http://127.0.0.1:5000
```

---

### Frontend:
```bash
cd frontend
python -m http.server 5500
```

Open browser:
```
http://127.0.0.1:5500
```

---

## 📡 API Endpoints

| Agent | Method | Endpoint | Description |
|-------|--------|-----------|-------------|
| Auto/Forced Router | POST | `/api/chat` | Core multi-agent API |
| Code Review Agent | POST | `/api/code-review` | Review code |
| Research Agent | POST | `/api/research` | Research a topic |
| Document Reader (PDF) | POST | `/api/upload-pdf` | Upload PDF |
| Document Reader (Text) | POST | `/api/document-text` | Summarize text |

---

## 🧪 Testing Examples


### Code Review
```
review my code:
def add(a,b): return a+b
```

### Topic Learning
```
teach me quick sort
```

### Research
```
research best resources to learn docker
```

### Document Reader
Upload a PDF or send:
```
summarize the following text:
...
```

---

## 🎯 Future Improvements

- Dark/Light mode  
- User authentication  
- Save chat history  
- Export notes to PDF  
- Voice-based chat  
- Agent chaining  

---

## 🤝 Contributing
Pull requests are welcome!



## 🎉 Final Notes

This system demonstrates:

- Multi-agent architecture  
- Real backend + frontend integration  
- PDF processing  
- Code analysis  
- Project generation  
- Research capabilities  

A complete **AI capstone project** ready for portfolio, GitHub, and academic submission.

⚠️ NOTICE: Forking is allowed only for educational viewing.
Do not reuse or redistribute this project without permission.
© 2025 Keval Ramoliya
