# Autonomous Scholarship–Student Matching Agent

Initial project scaffold. Frontend and backend run independently. AI agents, LangGraph, PostgreSQL/pgvector, and Playwright are planned but not implemented yet.

## Architecture

| Layer | Stack |
| --- | --- |
| Frontend | Next.js + TypeScript + Tailwind CSS |
| Backend | Python + FastAPI |
| Future AI | LLM + LangGraph |
| Database | PostgreSQL + pgvector |
| Automation | Playwright |

## Repository layout

```text
frontend/    Next.js app
backend/     FastAPI app
agents/      Future multi-agent logic
database/    Future models and DB configuration
data/        Scholarship and internship test datasets
docs/        Project documentation
```

## Prerequisites

- Node.js 20+
- Python 3.11+

Copy environment variable names from `.env.example` when you start wiring services. The apps do not require a `.env` file to start.

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Run the backend

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Health check: [http://localhost:8000/health](http://localhost:8000/health)

Expected response:

```json
{
  "status": "ok",
  "service": "scholarship-agent-backend"
}
```

Interactive API docs (FastAPI default): [http://localhost:8000/docs](http://localhost:8000/docs)
