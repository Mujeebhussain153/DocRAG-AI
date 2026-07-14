from uuid import uuid4
from app.db.base import Base
from sqlalchemy import ForeignKey, String, DateTime
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

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
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

    status: Mapped[str] = mapped_column(
        String(50),
        default="UPLOADED",
        nullable=False
    )

    # Python relationship
    owner = relationship(
        "User",
        back_populates="documents"
    )