from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
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
