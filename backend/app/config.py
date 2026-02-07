"""
GeoExplore-AI  —  App Configuration
====================================
Reads from .env via pydantic-settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # OpenAI
    OPENAI_API_KEY: str = ""

    # ArcGIS
    ARCGIS_API_KEY: str = ""
    ARCGIS_CLIENT_ID: str = ""
    ARCGIS_CLIENT_SECRET: str = ""

    # App
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:5173"

    # Database
    DATABASE_URL: str = "sqlite:///./geoexplore.db"


settings = Settings()
