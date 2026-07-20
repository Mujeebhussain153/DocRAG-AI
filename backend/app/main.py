from fastapi import FastAPI
from app.core.config import settings
from contextlib import asynccontextmanager
from app.db.base import Base
from app.db.database import engine
from app.api.v1.documents import router as document_router
import app.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """

    yield

    print("Shutting Down DOCRAG-AI")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

app.include_router(
    document_router,
    prefix="/api/v1"
)

@app.get("/")
def hello():
    return{
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION
    }

@app.get("/health")
def health():
    """
    Simple health endpoint.
    """
    return {
        "status": "healthy"
    }
