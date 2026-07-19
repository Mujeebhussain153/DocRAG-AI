from sqlalchemy.orm import Session
from pathlib import Path
from app.repositories.document_repository import DocumentRepository

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