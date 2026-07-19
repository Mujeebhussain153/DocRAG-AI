from uuid import uuid4
from app.db.base import Base
from sqlalchemy import ForeignKey, String, DateTime, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Document(Base):
    """
    Represents an uploaded document.
    """

    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default = lambda: str(uuid4())
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    extension: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable= False
    )

    storage_path: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    # Foreign Key
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate= func.now()
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="UPLOADED",
        nullable=False
    )

    error_message: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable= False
    )

    # Python relationship
    owner = relationship(
        "User",
        back_populates="documents"
    )