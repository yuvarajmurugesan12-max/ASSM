from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.core import engine, Base
from app.routes import students, opportunities, agents
from app.models import student, opportunity # Ensure models are registered with Base

# Create all tables in the database (simple migration/init support)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Scholarship Agent Backend",
    description="API for the Autonomous Scholarship–Student Matching Agent.",
    version="0.1.0",
)

# Enable CORS for the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)
app.include_router(opportunities.router)
app.include_router(agents.router)

@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "scholarship-agent-backend",
    }
