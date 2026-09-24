from app.agents.search_agent.state import SearchAgentState
from app.agents.search_agent.service import get_source
from app.database.core import SessionLocal
from app.models.opportunity import Opportunity, EligibilityRequirement, RequiredDocument
import datetime
import logging

logger = logging.getLogger(__name__)

async def search_source(state: SearchAgentState) -> SearchAgentState:
    logger.info(f"Searching source {state['source']} for {state['query']}")
    source = get_source(state["source"])
    results = await source.search(state["query"])
    
    return {
        **state,
        "raw_results": results,
        "status": "extracted"
    }

async def extract_opportunity(state: SearchAgentState) -> SearchAgentState:
    # In a real agent, this uses LLM to extract from raw HTML/text.
    # For MVP, we just pass through structured data.
    return {
        **state,
        "extracted_opportunities": state["raw_results"],
        "status": "extracted"
    }

async def normalize_opportunity(state: SearchAgentState) -> SearchAgentState:
    normalized = []
    for opp in state["extracted_opportunities"]:
        # Normalize fields
        norm_opp = {
            "title": opp.get("title", "").strip(),
            "provider": opp.get("provider", "").strip(),
            "opportunity_type": opp.get("opportunity_type", "scholarship").lower(),
            "description": opp.get("description", ""),
            "application_url": opp.get("application_url", ""),
            "source_url": opp.get("source_url", ""),
            "location": opp.get("location", None),
            "deadline": opp.get("deadline", None),
            "status": opp.get("status", "open"),
            "requirements": opp.get("requirements", []),
            "documents": opp.get("documents", [])
        }
        normalized.append(norm_opp)
    
    return {
        **state,
        "normalized_opportunities": normalized,
        "status": "normalized"
    }

async def validate_opportunity(state: SearchAgentState) -> SearchAgentState:
    valid = []
    errors = []
    
    for opp in state["normalized_opportunities"]:
        is_valid = True
        error_msg = ""
        
        if not opp["title"]:
            is_valid, error_msg = False, "Missing title"
        elif not opp["provider"]:
            is_valid, error_msg = False, "Missing provider"
        elif not opp["application_url"]:
            is_valid, error_msg = False, "Missing application_url"
        elif opp["opportunity_type"] not in ["scholarship", "internship", "fellowship"]:
            is_valid, error_msg = False, "Invalid opportunity_type"
            
        if is_valid:
            try:
                if opp["deadline"]:
                    # check if parseable
                    datetime.datetime.fromisoformat(opp["deadline"])
            except ValueError:
                is_valid, error_msg = False, "Invalid deadline format"
                
        if is_valid:
            valid.append(opp)
        else:
            errors.append({"opportunity": opp, "error": error_msg})
            
    return {
        **state,
        "normalized_opportunities": valid, # Overwrite with only valid
        "validation_errors": errors,
        "status": "validated"
    }

async def check_duplicate(state: SearchAgentState) -> SearchAgentState:
    db = SessionLocal()
    unique = []
    duplicates = []
    
    try:
        for opp in state["normalized_opportunities"]:
            # Check by title, provider, application_url
            existing = db.query(Opportunity).filter(
                Opportunity.title == opp["title"],
                Opportunity.provider == opp["provider"]
            ).first()
            
            if existing:
                duplicates.append(opp)
            else:
                unique.append(opp)
    finally:
        db.close()
        
    return {
        **state,
        "normalized_opportunities": unique,
        "duplicate_results": duplicates,
        "status": "duplicates_checked"
    }

async def save_opportunity(state: SearchAgentState) -> SearchAgentState:
    db = SessionLocal()
    saved = []
    
    try:
        for opp_data in state["normalized_opportunities"]:
            db_opp = Opportunity(
                title=opp_data["title"],
                provider=opp_data["provider"],
                opportunity_type=opp_data["opportunity_type"],
                description=opp_data["description"],
                application_url=opp_data["application_url"],
                source_url=opp_data["source_url"],
                location=opp_data["location"]
            )
            
            if opp_data["deadline"]:
                db_opp.deadline = datetime.datetime.fromisoformat(opp_data["deadline"])
                
            db.add(db_opp)
            db.commit()
            db.refresh(db_opp)
            
            for req in opp_data.get("requirements", []):
                db_req = EligibilityRequirement(
                    opportunity_id=db_opp.id,
                    requirement_type=req["requirement_type"],
                    requirement_value=req["requirement_value"],
                    operator=req.get("operator", "=="),
                    description=req.get("description", "")
                )
                db.add(db_req)
                
            for doc in opp_data.get("documents", []):
                db_doc = RequiredDocument(
                    opportunity_id=db_opp.id,
                    document_name=doc["document_name"],
                    document_type=doc.get("document_type", "PDF"),
                    mandatory=doc.get("mandatory", True),
                    description=doc.get("description", "")
                )
                db.add(db_doc)
                
            db.commit()
            saved.append(opp_data)
            
    finally:
        db.close()
        
    return {
        **state,
        "saved_opportunities": saved,
        "status": "completed"
    }
