from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime

class SearchRequest(BaseModel):
    query: str
    source: str = "demo"

class SearchResponse(BaseModel):
    status: str
    found: int
    new: int
    duplicates: int

class SearchStatusResponse(BaseModel):
    status: str
    query: Optional[str] = None
    found: int = 0
    new: int = 0
    duplicates: int = 0
