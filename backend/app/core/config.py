from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

# backend/app/core/config.py -> parents[2] resolves to the backend/ directory
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    """
    Central configuration for the application.

    BaseSettings automatically reads values from environment variables
    and the .env file.
    """

    # -----------------------------
    # Application Settings
    # -----------------------------
    APP_NAME: str
    APP_VERSION: str

    # -----------------------------
    # PostgreSQL Settings
    # -----------------------------
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: str


    # -----------------------------
    # Qdrant Settings
    # -----------------------------
    QDRANT_HOST: str
    QDRANT_PORT: int

    # Tell Pydantic where to find the .env file
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
    )

# Create a single settings object for the whole application.
settings = Settings()
