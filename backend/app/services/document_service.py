from sqlalchemy.orm import Session
from pathlib import Path
from uuid import uuid4
import aiofiles
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from fastapi import UploadFile, HTTPException

class DocumentService:
    """
    Handles document upload business logic.
    """

    def __init__(self, repository: DocumentRepository):

        self.repository = repository

        # Directory where uploaded files will be stored
        self.upload_directory = Path("app/uploads")

        # Create the directory if it doesn't already exist
        self.upload_directory.mkdir(
            parents=True,
            exist_ok=True
        )
    
    # Save Meta Data of the Document to DB by validating
    def uploadDocument(
            self,
            db:  Session,
            file: UploadFile,
            user_id: str
    ) -> Document:
        """
        Upload a document.

        Steps:
        1. Validate file
        2. Generate UUID
        3. Save file
        4. Save metadata
        5. Return document
        """
        allowed_extensions = {".pdf"}
        # Checking for the .pdf extension
        extension = Path(file.filename).suffix.lower()
        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed." 
            )
        # Checking for the Mime Type
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Invalid MIME Type" 
            )
        
        stored_filename = self._generateFileName(file.filename)

        # Saving the File
        saved_path = self._save_file(file=file, stored_filename=stored_filename)

        try:
            # Creating a Document Model
            document = Document(
                original_filename = file.filename,
                stored_filename = stored_filename,
                storage_path = str(saved_path),
                file_size = saved_path.stat().st_size,
                mime_type = file.content_type,
                status = "UPLOADED",
                error_message = None,
                user_id = user_id
            )

            # Saving MetaData to Postgres
            created_document = self.repository.create(
                db=db,
                document=document
            )

            return created_document
        
        except Exception:
            if saved_path.exists():
                saved_path.unlink()
            raise

    # Generate a UUID File name
    def _generateFileName(
            self,
            original_filename: str,
    ) -> str:
        """
        Generates a unique filename while preserving the extension.
        """

        extension = Path(original_filename).suffix

        return f"{uuid4()}{extension}"
    
    # Method for Saving the File Locally To The Uploads
    async def _save_file(
            self,
            file: UploadFile,
            stored_filename: str
    ) -> Path:
        """
        Saves the uploaded file to disk.
        """
        destination = self.upload_directory/stored_filename

        async with aiofiles.open(destination, "wb") as out_file:
            while chunk := await file.read(1024 * 1024):
                await out_file.write(chunk)
        
        return destination
        