# DiscoveryAI 🚀

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-18.x-61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688)

## 📋 Overview

**DiscoveryAI** is an AI-powered digital product discovery platform designed to automate the early stages of software development, including requirement gathering, analysis, design modeling, and partial code generation. 

Instead of manually writing requirements and documentation, users describe their idea in natural language, and DiscoveryAI uses Natural Language Processing (NLP) and AI models to transform that input into structured Software Requirements Specification (SRS) content, design artifacts, and sample backend/frontend code.

---

## ✨ Features

- **Natural Language Input**: Users can describe software ideas in free-text format
- **Automated Requirement Extraction**: Uses NLP to extract and classify requirements
- **Requirement Classification**: Categorizes requirements by type (functional/non-functional)
- **Documentation Generation**: Automatically generates summaries, use case descriptions, and user stories
- **Design Artifacts**: Generates diagrams, wireframes, and user flows
- **Code Generation**: Produces partial backend and frontend boilerplate code
- **Export Functionality**: Export generated requirements and documentation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React.js 18.x, Vite |
| **Backend** | FastAPI (Python) |
| **AI/NLP** | OpenAI GPT Models |
| **Database** | MongoDB |
| **API** | REST |

---

## 📁 Project Structure

```
Adv Software/
├── adv final project.pdf          # Project documentation report
├── backend main-1.py               # FastAPI backend application
├── Frontend App-1.jsx             # React frontend component
└── README.md                       # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- MongoDB (local or cloud instance)
- OpenAI API Key

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install fastapi pydantic uvicorn
```

5. Run the backend server:
```bash
python backend main-1.py
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd Frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check endpoint |
| `POST` | `/generate-requirements` | Generate requirements from user input |
| `GET` | `/projects/{id}` | Get project by ID |
| `POST` | `/export` | Export documentation |

---

## 📖 Usage

1. **Enter Project Description**: User provides a high-level description of their software idea
2. **AI Processing**: System extracts requirements using NLP
3. **Review Requirements**: User can refine, accept, or edit generated content
4. **Generate Artifacts**: System suggests diagrams and logical groupings
5. **Export**: User exports documentation (SRS, PDF, DOCX)

---

## 📱 User Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │────▶│   System    │────▶│   Review    │
│   Input     │     │   AI        │     │   Output    │
└─────────────┘     └─────────────┘     └─────────────┘
                                                │
                                                ▼
                    ┌─────────────┐     ┌─────────────┐
                    │   Export    │◀────│   Refine    │
                    │   Docs      │     │   Content   │
                    └─────────────┘     └─────────────┘
```

---

## 👥 Team Members

- **Sowjanya Kamtam** - 000798156
- **Harsha Guduru** - 000797805  
- **Darshan Joshi** - 000797697

---

## 📄 Documentation

For detailed project documentation, please refer to [adv final project.pdf](./adv%20final%20project.pdf)

---

## ⚠️ Limitations

- Generated code requires human review
- Edge cases, security, and validations must be manually added
- Depends on OpenAI API for NLP capabilities

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is for educational purposes.

---

## 🙏 Acknowledgments

-感谢 Professor 的指导
-感谢团队成员的辛勤工作
-感谢开源社区提供的工具和框架

---

*Built with ❤️ using FastAPI & React*

