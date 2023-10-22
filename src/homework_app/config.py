"""Config configuration."""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings from .env file"""

    env_name: str = "Local"
    base_url: str = "http://localhost:8000"

    class Config:  # pylint: disable=too-few-public-methods
        """Config file"""

        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """Cached settings"""
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
