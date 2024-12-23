from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    bsky_username: str
    bsky_password: str
    api_token: str

    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
