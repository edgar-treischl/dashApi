# dashApi/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Dash API"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    database_url: str = "sqlite:///./test.db"
    api_key: str | None = None  # Optional API key

    class Config:
        env_file = ".env"  # Automatically load from .env file if present
        env_file_encoding = "utf-8"


settings = Settings()
