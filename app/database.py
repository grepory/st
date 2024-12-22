import os
from databases import Database
from sqlalchemy import MetaData, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)