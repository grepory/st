from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./st.db"

settings = Settings()
