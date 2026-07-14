from uuid import uuid4
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base

class User(Base):
    """
    SQL Alchemy Table Represents users table
    """

    __tablename__ = "users"

    documents = relationship(
        "Document",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    # Primary Key
    id: Mapped[str] = mapped_column(
        String,
        primary_key = True,
        default = lambda :str(uuid4())
    )

    # Personal Information
    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    # Never store raw passwords!
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )