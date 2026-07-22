# 📄 Resume Screening AI

An end-to-end AI-powered Resume Screening and Question Answering system built using **FastAPI**, **Retrieval-Augmented Generation (RAG)**, **Sentence Transformers**, **FAISS**, **PostgreSQL**, and **Google Gemini**.

The application allows users to upload resumes, generates semantic embeddings, performs vector similarity search using FAISS, and answers questions about the uploaded resumes using Google's Gemini LLM.

---

# 🚀 Features

* 📂 Upload PDF resumes
* 📑 Extract text from resumes
* ✂️ Intelligent text chunking
* 🧠 Generate semantic embeddings using Sentence Transformers
* 🔍 Fast semantic search using FAISS
* 🤖 AI-powered question answering with Google Gemini
* 🗄️ PostgreSQL integration for metadata storage
* ⚡ REST APIs built with FastAPI
* 🐳 Docker & Docker Compose support
* 🔐 Modular backend architecture

---

# 🛠️ Tech Stack

### Backend

* Python 3.11
* FastAPI
* Uvicorn

### AI / Machine Learning

* SentenceTransformers
* FAISS
* Google Gemini API

### Database

* PostgreSQL
* SQLAlchemy ORM

### Deployment

* Docker
* Docker Compose

---

# 📁 Project Structure

```text
resume-screening/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── database/
│   ├── services/
│   ├── schemas/
│   └── utils/
│
├── uploads/
├── faiss_index/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── .env.example
└── README.md
```

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
                FastAPI Backend
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
PostgreSQL      SentenceTransformer   Gemini API
        │             │
        └─────────────▼
              FAISS Vector Store
                      │
                      ▼
               AI Generated Response
```

---

# 🔄 Application Workflow

1. User uploads a PDF resume.
2. Text is extracted from the document.
3. The extracted text is divided into smaller chunks.
4. Sentence Transformer converts each chunk into vector embeddings.
5. Embeddings are stored in a FAISS index.
6. User asks questions about the resume.
7. Relevant chunks are retrieved using semantic similarity.
8. Retrieved context is sent to Google Gemini.
9. Gemini generates the final response.
10. The API returns the answer to the user.

---

# 🐳 Running with Docker

## Build the project

```bash
docker compose build
```

## Start the application

```bash
docker compose up
```

## Stop the application

```bash
docker compose down
```

FastAPI will be available at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# ⚙️ Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/resume_db

POSTGRES_DB=resume_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password

GEMINI_API_KEY=YOUR_API_KEY
```

---

# 📌 API Overview

### Resume APIs

* Upload Resume
* List Uploaded Resumes

### AI APIs

* Ask Questions about Resume
* Retrieve AI Responses

---

# 🚀 Future Improvements

* JWT Authentication
* User Registration & Login
* Role-Based Access Control
* Resume History
* AWS S3 Storage
* Redis Caching
* Celery Background Tasks
* OCR Support for Scanned PDFs
* MLflow Integration
* Prometheus & Grafana Monitoring
* GitHub Actions CI/CD
* Kubernetes Deployment

---

# 💡 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* FastAPI REST APIs
* SQLAlchemy ORM
* PostgreSQL
* Docker & Docker Compose
* API Design
* AI Integration
* Modular Backend Development

---

# 👨‍💻 Author

**Krishnakant Mishra**

If you found this project helpful, consider giving it a ⭐ on GitHub.
