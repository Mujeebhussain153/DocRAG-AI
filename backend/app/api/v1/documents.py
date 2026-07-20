from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.services.document_service import DocumentService
from app.schemas.document import DocumentUploadResponse
from app.db.database import get_db

router = APIRouter(
    prefix="/documents",
    tags= ["Documents"]
)


@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(
        file: UploadFile = File(...),
        db: Session = Depends(get_db),    
):
    service = DocumentService()
    document = await service.uploadDocument(
        db=db,
        file=file,
        user_id= "dummy-user_id"
    )

    return DocumentUploadResponse.model_validate(document)