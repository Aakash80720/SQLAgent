
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    DATABASE_URL: str 
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "allow"
# Initialize settings

settings = Settings()