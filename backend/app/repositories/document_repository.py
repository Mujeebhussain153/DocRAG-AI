from sqlalchemy.orm import Session
from app.models.document import Document

class DocumentRepository:
    def create(
            self,
            db: Session,
            document: Document,
            status: str      
    ) -> Document:
        document.status = status
        
        db.add(document)

        db.commit()

        db.refresh(document)
        
        return document