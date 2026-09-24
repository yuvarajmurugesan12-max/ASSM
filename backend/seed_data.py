import sys
import os
import json
from datetime import datetime, timezone

# Add backend directory to sys.path so we can import app modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database.core import engine, SessionLocal
from app.models.opportunity import Opportunity, EligibilityRequirement, RequiredDocument
from app.models.student import Student, Skill, Document # Ensure they are registered

def seed_data():
    db = SessionLocal()
    try:
        # Check if opportunities already exist to avoid duplicating
        existing_count = db.query(Opportunity).count()
        if existing_count > 0:
            print(f"Database already contains {existing_count} opportunities. Skipping seed.")
            return

        print("Seeding 10 test opportunities into the database...")

        test_data = [
            {
                "title": "Future Innovators Demo Scholarship",
                "provider": "Tech Foundation",
                "opportunity_type": "scholarship",
                "description": "[TEST DATA] A demo scholarship for engineering students interested in innovation and technology.",
                "application_url": "http://example.com/apply/future-innovators",
                "source_url": "http://example.com/future-innovators",
                "location": "Global",
                "deadline": datetime(2026, 12, 15, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "cgpa", "requirement_value": "7.0", "operator": ">=", "description": "Minimum CGPA of 7.0"},
                    {"requirement_type": "course", "requirement_value": "Engineering", "operator": "==", "description": "Must be enrolled in an Engineering course"}
                ],
                "documents": [
                    {"document_name": "Academic Transcript", "document_type": "PDF", "mandatory": True, "description": "Latest academic transcript"},
                    {"document_name": "Statement of Purpose", "document_type": "PDF", "mandatory": True, "description": "500-word essay on innovation"}
                ]
            },
            {
                "title": "Global Leaders Fellowship (TEST)",
                "provider": "Global Institute",
                "opportunity_type": "fellowship",
                "description": "[TEST DATA] Fellowship for students demonstrating outstanding leadership skills.",
                "application_url": "http://example.com/apply/global-leaders",
                "source_url": "http://example.com/global-leaders",
                "location": "New York, USA",
                "deadline": datetime(2027, 3, 1, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "year", "requirement_value": "4", "operator": "==", "description": "Final year students only"},
                    {"requirement_type": "skill", "requirement_value": "Leadership", "operator": "contains", "description": "Demonstrated leadership skills"}
                ],
                "documents": [
                    {"document_name": "Resume/CV", "document_type": "PDF", "mandatory": True, "description": "Updated Resume"},
                    {"document_name": "Letter of Recommendation", "document_type": "PDF", "mandatory": True, "description": "From a professor or employer"}
                ]
            },
            {
                "title": "Summer Tech Internship (Demo)",
                "provider": "TechCorp Solutions",
                "opportunity_type": "internship",
                "description": "[TEST DATA] A 3-month summer internship for computer science students.",
                "application_url": "http://example.com/apply/summer-tech",
                "source_url": "http://example.com/summer-tech",
                "location": "Remote",
                "deadline": datetime(2027, 4, 15, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "course", "requirement_value": "Computer Science", "operator": "==", "description": "CS Majors"},
                    {"requirement_type": "skill", "requirement_value": "Python", "operator": "contains", "description": "Proficiency in Python"}
                ],
                "documents": [
                    {"document_name": "Resume", "document_type": "PDF", "mandatory": True, "description": "Detailed CV with projects"}
                ]
            },
            {
                "title": "Women in STEM Grant (Test)",
                "provider": "STEM Women Org",
                "opportunity_type": "scholarship",
                "description": "[TEST DATA] Financial support for women pursuing STEM degrees.",
                "application_url": "http://example.com/apply/women-stem",
                "source_url": "http://example.com/women-stem",
                "location": "Global",
                "deadline": datetime(2026, 11, 30, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "category", "requirement_value": "Female", "operator": "==", "description": "Female applicants only"},
                    {"requirement_type": "branch", "requirement_value": "Science, Technology, Engineering, Math", "operator": "in", "description": "STEM branches"}
                ],
                "documents": [
                    {"document_name": "Identity Proof", "document_type": "PDF", "mandatory": True, "description": "Government issued ID"}
                ]
            },
            {
                "title": "Local Community Service Award (Demo)",
                "provider": "City Council",
                "opportunity_type": "scholarship",
                "description": "[TEST DATA] Award for students with over 100 hours of community service.",
                "application_url": "http://example.com/apply/local-award",
                "source_url": "http://example.com/local-award",
                "location": "Local City",
                "deadline": datetime(2027, 1, 15, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "location", "requirement_value": "Local City", "operator": "==", "description": "Resident of Local City"}
                ],
                "documents": [
                    {"document_name": "Service Certificate", "document_type": "PDF", "mandatory": True, "description": "Proof of community service hours"}
                ]
            },
            {
                "title": "Data Science Research Fellowship (Test)",
                "provider": "Data Research Lab",
                "opportunity_type": "fellowship",
                "description": "[TEST DATA] 1-year research fellowship focusing on AI and ML.",
                "application_url": "http://example.com/apply/ds-fellowship",
                "source_url": "http://example.com/ds-fellowship",
                "location": "London, UK",
                "deadline": datetime(2027, 2, 28, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "cgpa", "requirement_value": "8.5", "operator": ">=", "description": "High academic standing required"},
                    {"requirement_type": "skill", "requirement_value": "Machine Learning", "operator": "contains", "description": "Prior ML experience"}
                ],
                "documents": [
                    {"document_name": "Research Proposal", "document_type": "PDF", "mandatory": True, "description": "2-page proposal"}
                ]
            },
            {
                "title": "Creative Arts Demo Grant",
                "provider": "Arts Foundation",
                "opportunity_type": "scholarship",
                "description": "[TEST DATA] Grant to support students in fine arts and design.",
                "application_url": "http://example.com/apply/arts-grant",
                "source_url": "http://example.com/arts-grant",
                "location": "Global",
                "deadline": datetime(2026, 10, 31, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "course", "requirement_value": "Fine Arts", "operator": "==", "description": "Enrolled in Arts program"}
                ],
                "documents": [
                    {"document_name": "Portfolio", "document_type": "URL", "mandatory": True, "description": "Link to digital portfolio"}
                ]
            },
            {
                "title": "Finance Analyst Internship (TEST)",
                "provider": "Global Bank",
                "opportunity_type": "internship",
                "description": "[TEST DATA] Summer internship for aspiring financial analysts.",
                "application_url": "http://example.com/apply/finance-intern",
                "source_url": "http://example.com/finance-intern",
                "location": "New York, USA",
                "deadline": datetime(2027, 1, 10, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "branch", "requirement_value": "Finance", "operator": "==", "description": "Finance majors"},
                    {"requirement_type": "year", "requirement_value": "3", "operator": "==", "description": "Pre-final year students"}
                ],
                "documents": [
                    {"document_name": "Cover Letter", "document_type": "PDF", "mandatory": True, "description": "Explaining interest in finance"}
                ]
            },
            {
                "title": "Needs-Based Education Fund (Demo)",
                "provider": "EduCare NGO",
                "opportunity_type": "scholarship",
                "description": "[TEST DATA] Financial assistance for students from low-income families.",
                "application_url": "http://example.com/apply/need-fund",
                "source_url": "http://example.com/need-fund",
                "location": "National",
                "deadline": datetime(2026, 12, 1, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "income", "requirement_value": "50000", "operator": "<=", "description": "Family income below threshold"}
                ],
                "documents": [
                    {"document_name": "Income Certificate", "document_type": "PDF", "mandatory": True, "description": "Official income proof"}
                ]
            },
            {
                "title": "Young Entrepreneurs Fellowship (Test)",
                "provider": "Startup Incubator",
                "opportunity_type": "fellowship",
                "description": "[TEST DATA] Support and mentorship for student founders.",
                "application_url": "http://example.com/apply/young-entrepreneurs",
                "source_url": "http://example.com/young-entrepreneurs",
                "location": "San Francisco, USA",
                "deadline": datetime(2027, 5, 1, tzinfo=timezone.utc),
                "requirements": [
                    {"requirement_type": "age", "requirement_value": "25", "operator": "<=", "description": "Under 25 years old"}
                ],
                "documents": [
                    {"document_name": "Pitch Deck", "document_type": "PDF", "mandatory": True, "description": "Startup idea pitch deck"}
                ]
            }
        ]

        for data in test_data:
            reqs = data.pop("requirements")
            docs = data.pop("documents")
            
            opp = Opportunity(**data)
            db.add(opp)
            db.flush() # get id
            
            for req in reqs:
                db.add(EligibilityRequirement(**req, opportunity_id=opp.id))
                
            for doc in docs:
                db.add(RequiredDocument(**doc, opportunity_id=opp.id))
                
        db.commit()
        print("Successfully seeded 10 test opportunities!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
