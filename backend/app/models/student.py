from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.core import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    college = Column(String, nullable=True)
    course = Column(String, nullable=True)
    branch = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    semester = Column(Integer, nullable=True)
    percentage = Column(Float, nullable=True)
    cgpa = Column(Float, nullable=True)
    preferred_opportunity_type = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    skills = relationship("Skill", back_populates="student", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="student", cascade="all, delete-orphan")

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    skill_name = Column(String, index=True)

    student = relationship("Student", back_populates="skills")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    document_name = Column(String)
    document_type = Column(String)
    uploaded = Column(DateTime(timezone=True), server_default=func.now())
    file_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("Student", back_populates="documents")
