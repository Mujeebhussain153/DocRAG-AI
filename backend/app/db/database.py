""""
Responsible for Creating Engine, Sessions and Providing a Session for FASTAPI
"""
from sqlalchemy import create_engine # This Engine is response for making a connection
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

# -------------------------------------------------------------------
# Engine
# -------------------------------------------------------------------
# The Engine is responsible for managing connections to PostgreSQL.
# It does NOT execute business logic. Think of it as the gateway
# between SQLAlchemy and the database.
# -------------------------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL,
    echo = True # Logs generated SQL to the console
)

# -------------------------------------------------------------------
# Session Factory
# -------------------------------------------------------------------
# sessionmaker creates new Session objects when needed.
# Each API request will receive its own Session instance.
# -------------------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db():
    """
    FastAPI dependency that provides a database session.

    A new session is created for each request and is
    always closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db

    finally:
        
        db.close()



