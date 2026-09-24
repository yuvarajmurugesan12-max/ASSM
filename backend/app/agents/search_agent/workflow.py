from langgraph.graph import StateGraph, START, END
from app.agents.search_agent.state import SearchAgentState
from app.agents.search_agent.nodes import (
    search_source,
    extract_opportunity,
    normalize_opportunity,
    validate_opportunity,
    check_duplicate,
    save_opportunity
)

def build_search_graph():
    workflow = StateGraph(SearchAgentState)
    
    # Add nodes
    workflow.add_node("search_source", search_source)
    workflow.add_node("extract_opportunity", extract_opportunity)
    workflow.add_node("normalize_opportunity", normalize_opportunity)
    workflow.add_node("validate_opportunity", validate_opportunity)
    workflow.add_node("check_duplicate", check_duplicate)
    workflow.add_node("save_opportunity", save_opportunity)
    
    # Add edges
    workflow.add_edge(START, "search_source")
    workflow.add_edge("search_source", "extract_opportunity")
    workflow.add_edge("extract_opportunity", "normalize_opportunity")
    workflow.add_edge("normalize_opportunity", "validate_opportunity")
    workflow.add_edge("validate_opportunity", "check_duplicate")
    workflow.add_edge("check_duplicate", "save_opportunity")
    workflow.add_edge("save_opportunity", END)
    
    return workflow.compile()
