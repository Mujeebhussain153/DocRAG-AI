from datetime import datetime
from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    """
    Decides how the response is generated after a file is uploaded
    """
    id: str
    original_filename: str
    status: str
    created_at: datetime
    model_config = {
        "from_attributes": True
    }

