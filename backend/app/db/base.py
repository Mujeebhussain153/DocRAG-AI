from sqlalchemy.orm import DeclerativeBase

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Every model (User, Document, Collection, etc.)
    will inherit from this class.
    """

    pass