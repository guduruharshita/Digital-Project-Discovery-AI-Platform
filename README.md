# DiscoveryAI — AI-Powered Product Discovery Platform

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18.x-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)](https://mongodb.com)

## What It Does

**DiscoveryAI** takes a plain-English product description and generates structured software artifacts using GPT-4 — SRS documents, user stories, and boilerplate code scaffolding. It eliminates the blank-page problem for developers and product teams who need to move from idea to structured spec quickly.

## Features

- **Natural Language → SRS**: Structured functional and non-functional requirements from a single prompt
- **User Stories**: Persona-based stories broken down by feature area
- **Code Scaffolding**: Module-level boilerplate for your target stack
- **Copy/Export**: One-click copy of all generated artifacts

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 18, Vite, CSS |
| Backend | FastAPI (Python 3.9+) |
| AI | OpenAI GPT-4 API |
| Database | MongoDB |

## Project Structure

```
├── backend/
│   ├── main.py
│   ├── routes/
│   │   └── generate.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   │       ├── RequirementForm.jsx
│   │       └── RequirementOutput.jsx
│   ├── index.html
│   └── package.json
└── .gitignore
```

## How to Run Locally

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your OPENAI_API_KEY
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/artifact-types` | List supported types |
| POST | `/generate` | Generate artifacts from description |

## Author

**Harshita Guduru** — [GitHub](https://github.com/guduruharshita) · [LinkedIn](https://linkedin.com/in/harshita-guduru)
