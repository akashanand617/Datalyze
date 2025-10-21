from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Datalyze"
    VERSION: str = "1.0.0"
    
    # Database (placeholder - no database setup yet)
    DATABASE_URL: str = "sqlite:///./datalyze.db"
    
    # Redis (placeholder - no Redis setup yet)
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Celery (placeholder - no Celery setup yet)
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080"
    ]
    
    # File Upload
    MAX_FILE_SIZE: int = 10485760  # 10MB
    ALLOWED_FILE_TYPES: List[str] = ["csv", "xlsx", "xls"]
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    DEBUG: bool = True
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()
