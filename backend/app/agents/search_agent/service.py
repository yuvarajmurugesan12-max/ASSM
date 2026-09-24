from typing import List, Any
from abc import ABC, abstractmethod

class OpportunitySource(ABC):
    @abstractmethod
    async def search(self, query: str) -> List[Any]:
        pass

class DemoOpportunitySource(OpportunitySource):
    async def search(self, query: str) -> List[Any]:
        # Structured test opportunities
        return [
            {
                "title": f"Demo Scholarship for {query}",
                "provider": "Demo Foundation",
                "opportunity_type": "scholarship",
                "description": "This is a demo scholarship returned by the search agent.",
                "application_url": "http://demo.com/apply",
                "source_url": "http://demo.com",
                "location": "Global",
                "deadline": "2027-12-31T00:00:00",
                "status": "open",
                "requirements": [
                    {"requirement_type": "cgpa", "requirement_value": "3.5", "operator": ">=", "description": "Minimum CGPA"}
                ],
                "documents": [
                    {"document_name": "Resume", "document_type": "PDF", "mandatory": True, "description": "Updated resume"}
                ]
            },
            {
                "title": f"Engineering Fellowship {query}",
                "provider": "Demo Foundation",
                "opportunity_type": "fellowship",
                "description": "Fellowship for engineering students.",
                "application_url": "http://demo.com/apply-eng",
                "source_url": "http://demo.com",
                "location": "Remote",
                "deadline": "2028-01-01T00:00:00",
                "status": "open",
                "requirements": [],
                "documents": []
            }
        ]

class WebSearchOpportunitySource(OpportunitySource):
    async def search(self, query: str) -> List[Any]:
        # Future implementation using external API (e.g. SERP API)
        return []

def get_source(source_type: str) -> OpportunitySource:
    if source_type == "demo":
        return DemoOpportunitySource()
    elif source_type == "web":
        return WebSearchOpportunitySource()
    else:
        raise ValueError(f"Unknown source type: {source_type}")
