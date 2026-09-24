from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.core import get_db
from app.models.student import Student, Skill, Document
from app.schemas.student import (
    StudentCreate, StudentResponse, StudentUpdate, 
    SkillCreate, SkillResponse, DocumentCreate, DocumentResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get("", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_data = student_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)
    
    db.commit()
    db.refresh(student)
    return student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()

@router.post("/{student_id}/skills", response_model=SkillResponse, status_code=status.HTTP_201_CREATED)
def add_skill(student_id: int, skill: SkillCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_skill = Skill(**skill.model_dump(), student_id=student_id)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

@router.post("/{student_id}/documents", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def add_document(student_id: int, document: DocumentCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_document = Document(**document.model_dump(), student_id=student_id)
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document
