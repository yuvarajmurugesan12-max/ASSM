from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import List, Optional
from datetime import datetime

class EligibilityRequirementBase(BaseModel):
    requirement_type: str
    requirement_value: str
    operator: str
    description: Optional[str] = None

class EligibilityRequirementCreate(EligibilityRequirementBase):
    pass

class EligibilityRequirementResponse(EligibilityRequirementBase):
    id: int
    opportunity_id: int
    
    model_config = ConfigDict(from_attributes=True)

class RequiredDocumentBase(BaseModel):
    document_name: str
    document_type: Optional[str] = None
    mandatory: bool = True
    description: Optional[str] = None

class RequiredDocumentCreate(RequiredDocumentBase):
    pass

class RequiredDocumentResponse(RequiredDocumentBase):
    id: int
    opportunity_id: int
    
    model_config = ConfigDict(from_attributes=True)

class OpportunityBase(BaseModel):
    title: str = Field(..., min_length=3, description="Title of the opportunity")
    provider: str = Field(..., min_length=2, description="Provider of the opportunity")
    opportunity_type: str = Field(..., description="scholarship, internship, or fellowship")
    description: Optional[str] = None
    application_url: Optional[str] = None
    source_url: Optional[str] = None
    location: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = "open"
    
class OpportunityCreate(OpportunityBase):
    @field_validator('opportunity_type')
    @classmethod
    def validate_type(cls, value):
        if value not in ["scholarship", "internship", "fellowship"]:
            raise ValueError("opportunity_type must be scholarship, internship, or fellowship")
        return value

class OpportunityUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3)
    provider: Optional[str] = Field(None, min_length=2)
    opportunity_type: Optional[str] = None
    description: Optional[str] = None
    application_url: Optional[str] = None
    source_url: Optional[str] = None
    location: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = None

class OpportunityResponse(OpportunityBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    requirements: List[EligibilityRequirementResponse] = []
    documents: List[RequiredDocumentResponse] = []

    model_config = ConfigDict(from_attributes=True)
