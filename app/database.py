import os
from databases import Database
from sqlalchemy import MetaData, create_engine

from app.core.config import settings

database = Database(settings.database_url)
metadata = MetaData()
engine = create_engine(settings.database_url)