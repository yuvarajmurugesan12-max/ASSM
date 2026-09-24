from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class SkillBase(BaseModel):
    skill_name: str

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int
    student_id: int
    
    model_config = ConfigDict(from_attributes=True)


class DocumentBase(BaseModel):
    document_name: str
    document_type: str
    file_url: Optional[str] = None

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: int
    student_id: int
    uploaded: Optional[datetime] = None
    created_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class StudentBase(BaseModel):
    full_name: str
    email: str
    age: Optional[int] = None
    location: Optional[str] = None
    college: Optional[str] = None
    course: Optional[str] = None
    branch: Optional[str] = None
    year: Optional[int] = None
    semester: Optional[int] = None
    percentage: Optional[float] = None
    cgpa: Optional[float] = None
    preferred_opportunity_type: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    full_name: Optional[str] = None
    email: Optional[str] = None

class StudentResponse(StudentBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    skills: List[SkillResponse] = []
    documents: List[DocumentResponse] = []

    model_config = ConfigDict(from_attributes=True)
