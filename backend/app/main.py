from fastapi import FastAPI
from app.core.config import settings
from contextlib import asynccontextmanager
from app.db.base import Base
from app.db.database import engine
import app.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """
    Base.metadata.create_all(bind=engine)

    yield

    print("Shutting Down DOCRAG-AI")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
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
