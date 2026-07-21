from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks
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
        background_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
):
    service = DocumentService()
    document = await service.uploadDocument(
        db=db,
        file=file,
        user_id= "dummy-user_id"
    )

    background_tasks.add_task(
        service.process_document,
        document.id
    )

    return DocumentUploadResponse.model_validate(document)