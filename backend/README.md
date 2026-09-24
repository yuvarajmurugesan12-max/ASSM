# Backend

FastAPI service for the Autonomous Scholarship–Student Matching Agent.

## Setup

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Health check: http://localhost:8000/health
