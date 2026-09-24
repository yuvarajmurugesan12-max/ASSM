from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Optional
from app.agents.search_agent.schemas import SearchRequest, SearchResponse, SearchStatusResponse
from app.agents.search_agent.workflow import build_search_graph
from app.agents.search_agent.state import SearchAgentState
import logging

router = APIRouter(prefix="/agents", tags=["Agents"])
logger = logging.getLogger(__name__)

# Simple in-memory state tracking for MVP status polling
# In production, this would use LangGraph's checkpointer/DB
LATEST_STATUS = {
    "status": "idle",
    "query": None,
    "found": 0,
    "new": 0,
    "duplicates": 0
}

search_graph = build_search_graph()

async def run_search_agent_bg(query: str, source: str):
    global LATEST_STATUS
    LATEST_STATUS = {
        "status": "running",
        "query": query,
        "found": 0,
        "new": 0,
        "duplicates": 0
    }
    
    initial_state: SearchAgentState = {
        "query": query,
        "source": source,
        "raw_results": [],
        "extracted_opportunities": [],
        "normalized_opportunities": [],
        "validation_errors": [],
        "duplicate_results": [],
        "saved_opportunities": [],
        "status": "started"
    }
    
    try:
        logger.info(f"Starting Search Agent for query: {query}")
        result = await search_graph.ainvoke(initial_state)
        
        LATEST_STATUS = {
            "status": "completed",
            "query": query,
            "found": len(result["raw_results"]),
            "new": len(result["saved_opportunities"]),
            "duplicates": len(result["duplicate_results"])
        }
        logger.info("Search Agent completed successfully.")
        
    except Exception as e:
        logger.error(f"Search Agent failed: {e}")
        LATEST_STATUS["status"] = f"error: {str(e)}"

@router.post("/search", response_model=SearchResponse)
async def start_search(request: SearchRequest, background_tasks: BackgroundTasks):
    # For MVP, we can run it synchronously if we want to return results immediately,
    # or asynchronously. The requirements ask for a response like:
    # { "status": "completed", "found": 10, "new": 8, "duplicates": 2 }
    # Let's run it synchronously so we can return the exact result.
    
    initial_state: SearchAgentState = {
        "query": request.query,
        "source": request.source,
        "raw_results": [],
        "extracted_opportunities": [],
        "normalized_opportunities": [],
        "validation_errors": [],
        "duplicate_results": [],
        "saved_opportunities": [],
        "status": "started"
    }
    
    try:
        result = await search_graph.ainvoke(initial_state)
        
        global LATEST_STATUS
        LATEST_STATUS = {
            "status": "completed",
            "query": request.query,
            "found": len(result["raw_results"]),
            "new": len(result["saved_opportunities"]),
            "duplicates": len(result["duplicate_results"])
        }
        
        return SearchResponse(
            status="completed",
            found=len(result["raw_results"]),
            new=len(result["saved_opportunities"]),
            duplicates=len(result["duplicate_results"])
        )
    except Exception as e:
        logger.error(f"Search Agent failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/status", response_model=SearchStatusResponse)
async def get_search_status():
    return SearchStatusResponse(**LATEST_STATUS)
