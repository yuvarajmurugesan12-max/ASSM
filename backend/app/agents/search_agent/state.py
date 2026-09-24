from typing import TypedDict, List, Any, Optional

class SearchAgentState(TypedDict):
    query: str
    source: str
    raw_results: List[Any]
    extracted_opportunities: List[Any]
    normalized_opportunities: List[dict]
    validation_errors: List[dict]
    duplicate_results: List[dict]
    saved_opportunities: List[dict]
    status: str
