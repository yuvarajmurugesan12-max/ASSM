from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.core import Base

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    provider = Column(String)
    opportunity_type = Column(String, index=True)  # scholarship / internship / fellowship
    description = Column(Text, nullable=True)
    application_url = Column(String, nullable=True)
    source_url = Column(String, nullable=True)
    location = Column(String, nullable=True)
    deadline = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, default="open")  # open / closed
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    requirements = relationship("EligibilityRequirement", back_populates="opportunity", cascade="all, delete-orphan")
    documents = relationship("RequiredDocument", back_populates="opportunity", cascade="all, delete-orphan")

class EligibilityRequirement(Base):
    __tablename__ = "eligibility_requirements"

    id = Column(Integer, primary_key=True, index=True)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"))
    requirement_type = Column(String, index=True) # age, course, branch, year, cgpa, percentage, location, income, category, skill
    requirement_value = Column(String)
    operator = Column(String) # >=, <=, ==, contains, in
    description = Column(String, nullable=True)

    opportunity = relationship("Opportunity", back_populates="requirements")

class RequiredDocument(Base):
    __tablename__ = "required_documents"

    id = Column(Integer, primary_key=True, index=True)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"))
    document_name = Column(String)
    document_type = Column(String, nullable=True)
    mandatory = Column(Boolean, default=True)
    description = Column(String, nullable=True)

    opportunity = relationship("Opportunity", back_populates="documents")
