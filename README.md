# DiscoveryAI — Digital Project Discovery Platform 🚀

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18.x-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)]()

---

## What It Does

**DiscoveryAI** is an AI-powered platform that takes a plain-English description of a software idea and automatically produces a structured Software Requirements Specification (SRS), use cases, user stories, and boilerplate code. It eliminates hours of manual requirements writing by leveraging GPT-4 to extract, classify, and document both functional and non-functional requirements — then generates matching frontend and backend scaffolding.

> Built as a capstone project demonstrating end-to-end AI-assisted software engineering.

---

## ✨ Key Features

- **Natural Language → SRS**: Describe your app idea; get a full requirements document
- **Requirement Classification**: Auto-categorizes functional vs. non-functional requirements
- **Code Generation**: Produces FastAPI backend + React frontend boilerplate
- **Export**: Download generated docs as PDF/DOCX
- **Design Artifacts**: Suggests user flows and logical component diagrams

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 18, Vite, JSX |
| Backend | FastAPI (Python 3.9+) |
| AI/NLP | OpenAI GPT-4 API |
| Database | MongoDB |
| API Style | REST |

---

## 🚀 How to Run Locally

### Prerequisites

- Python 3.9+
- Node.js 16+
- MongoDB running locally or a MongoDB Atlas URI
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the repo

```bash
git clone https://github.com/guduruharshita/Digital-Project-Discovery-AI-Platform.git
cd Digital-Project-Discovery-AI-Platform
```

### 2. Backend setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install fastapi uvicorn pydantic pymongo openai python-dotenv
echo "OPENAI_API_KEY=your_key_here" > .env
uvicorn "backend main-1":app --reload
```

Backend runs at `http://localhost:8000`

### 3. Frontend setup

```bash
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/generate-requirements` | Generate SRS from text input |
| `GET` | `/projects/{id}` | Fetch a saved project |
| `POST` | `/export` | Export documentation |

---

## 📁 Project Structure

```
Digital-Project-Discovery-AI-Platform/
├── backend main-1.py       # FastAPI application
├── Frontend App-1.jsx      # React frontend component
├── adv final project.pdf   # Full project documentation
└── README.md
```

---

## 👥 Team

- Sowjanya Kamtam
- Harshita Guduru
- Darshan Joshi

---

## ⚠️ Limitations

- Generated code requires human review before production use
- Requires an active OpenAI API key (usage costs apply)
- Security, edge-case handling, and validation must be added manually

---

## 📄 License

Educational use. See [adv final project.pdf](./adv%20final%20project.pdf) for full documentation.
