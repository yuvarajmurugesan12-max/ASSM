from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.core import get_db
from app.models.opportunity import Opportunity, EligibilityRequirement, RequiredDocument
from app.schemas.opportunity import (
    OpportunityCreate, OpportunityResponse, OpportunityUpdate,
    EligibilityRequirementCreate, EligibilityRequirementResponse,
    RequiredDocumentCreate, RequiredDocumentResponse
)

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)

@router.post("", response_model=OpportunityResponse, status_code=status.HTTP_201_CREATED)
def create_opportunity(opportunity: OpportunityCreate, db: Session = Depends(get_db)):
    new_opportunity = Opportunity(**opportunity.model_dump())
    db.add(new_opportunity)
    db.commit()
    db.refresh(new_opportunity)
    return new_opportunity

@router.get("", response_model=list[OpportunityResponse])
def get_opportunities(db: Session = Depends(get_db)):
    opportunities = db.query(Opportunity).all()
    return opportunities

@router.get("/{opportunity_id}", response_model=OpportunityResponse)
def get_opportunity(opportunity_id: int, db: Session = Depends(get_db)):
    opportunity = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opportunity

@router.put("/{opportunity_id}", response_model=OpportunityResponse)
def update_opportunity(opportunity_id: int, opportunity_update: OpportunityUpdate, db: Session = Depends(get_db)):
    opportunity = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    update_data = opportunity_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(opportunity, key, value)
    
    db.commit()
    db.refresh(opportunity)
    return opportunity

@router.delete("/{opportunity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_opportunity(opportunity_id: int, db: Session = Depends(get_db)):
    opportunity = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    db.delete(opportunity)
    db.commit()

@router.post("/{opportunity_id}/requirements", response_model=EligibilityRequirementResponse, status_code=status.HTTP_201_CREATED)
def add_requirement(opportunity_id: int, requirement: EligibilityRequirementCreate, db: Session = Depends(get_db)):
    opportunity = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    new_requirement = EligibilityRequirement(**requirement.model_dump(), opportunity_id=opportunity_id)
    db.add(new_requirement)
    db.commit()
    db.refresh(new_requirement)
    return new_requirement

@router.post("/{opportunity_id}/documents", response_model=RequiredDocumentResponse, status_code=status.HTTP_201_CREATED)
def add_document(opportunity_id: int, document: RequiredDocumentCreate, db: Session = Depends(get_db)):
    opportunity = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    new_document = RequiredDocument(**document.model_dump(), opportunity_id=opportunity_id)
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document
