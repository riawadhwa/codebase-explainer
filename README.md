# 🔍 RepoLens AI

**Understand any GitHub repository in minutes — architecture, execution flow, and setup explained in plain English.**

🌐 **Live Demo:** https://repolens-ai.onrender.com  
📦 **Backend + Frontend:** Single integrated deployment  
🧠 **LLM-powered agent system using PydanticAI**

---

## 🚀 What is RepoLens?

Dropping into a new codebase can be overwhelming — unclear structure, hidden entry points, undocumented flows.

**RepoLens AI** solves this by:

- Analyzing a **public GitHub repository**
- Understanding its **structure, architecture, and execution flow**
- Explaining **what it does, how it works, and how to run it**
- Presenting everything in a **clean, developer-friendly UI**

All explanations are generated dynamically using a **multi-agent AI system**.

---

## ✨ Key Features

- 🔗 Analyze any **public GitHub repository**
- 🧠 Agent-based reasoning using **PydanticAI**
- 🏗 Architecture breakdown (folders, responsibilities, entry points)
- 🔁 Execution flow explanation (startup → request lifecycle)
- ▶️ Run/setup commands inferred from `package.json`, `requirements.txt`, etc.

---

## 🧠 How It Works (High Level)

1. User inputs a **GitHub repository URL**
2. Backend:
   - Fetches repository metadata via **GitHub REST API**
   - Downloads the repository ZIP
   - Scans file structure (filtered, capped, and safe)
3. **AI agents analyze the repository**
4. Structured JSON output is generated
5. Frontend renders results across tabs:
   - **Overview**
   - **Architecture**
   - **Execution Flow**

---

## 🧩 Agent Architecture

RepoLens uses **multiple specialized agents**, each with a focused responsibility:

### 1️⃣ Project Classifier Agent

Determines:
- Project type (frontend / backend / full-stack)
- Primary language
- Frameworks
- Entry points

### 2️⃣ Architecture Analysis Agent

- Maps folder structure to responsibilities
- Identifies core components
- Infers design patterns and separation of concerns

### 3️⃣ Execution Flow Agent

- Explains how the application starts
- Describes request lifecycle
- Includes middleware, services, and database interactions

All agents are built using **PydanticAI** with strict output validation.

---

## 🛠 Tech Stack

### Backend
- **FastAPI**
- **PydanticAI**
- **Python 3.11**
- **Requests**
- **Uvicorn**
- **GitHub REST API**

### Frontend
- **React (Vite)**
- **Tailwind CSS**
- **Dark-first design**
- **Component-based architecture**

### Deployment
- **Render** 
- Frontend served from backend
- Server-side GitHub authentication

---

## 📁 Project Structure
```
repo-lens/
├── app/
│ ├── agents/ # AI agents (classifier, architecture, flow)
│ ├── api/ # FastAPI routes
│ ├── services/ # GitHub download & repo scanning
│ ├── schemas/ # Pydantic models
│ └── main.py # App entry point
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ └── tabs/ # Overview / Architecture / Execution Flow
│ │ ├── App.jsx
│ │ └── main.jsx
│ └── index.html
│
├── requirements.txt
└── README.md
```
---

## ▶️ Running Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/repo-lens.git
cd repo-lens
```
2️⃣ Backend setup
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file:

GITHUB_TOKEN=your_github_pat_here


Run the backend:

uvicorn app.main:app --reload

3️⃣ Frontend setup
cd frontend
npm install
npm run dev

👩‍💻 Author

Ria Wadhwa
B.Tech CSE @ SRM Institute of Science and Technology
Focused on full-stack systems, AI agents, and developer tooling

