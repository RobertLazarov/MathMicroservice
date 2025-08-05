from __future__ import annotations
from functools import lru_cache
from pathlib import Path
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SQLITE_PATH = PROJECT_ROOT / "requests.db"

class Settings(BaseSettings):
    app_name: str = "Math Operations Service"
    database_url: AnyUrl | str = Field(default=f"sqlite:///{DEFAULT_SQLITE_PATH}", env="DATABASE_URL")
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()
