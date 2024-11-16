from pydantic import BaseSettings

class Settings(BaseSettings):
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    DATABASE_URL: str = "sqlite:///./test.db"  # Use PostgreSQL in production
    GITHUB_TOKEN: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
