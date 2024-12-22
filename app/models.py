from sqlalchemy import Table, Column, String
from app.database import metadata

link_mappings = Table(
    "link_mappings",
    metadata,
    Column("slug", String, primary_key=True),
    Column("url", String, nullable=False, unique=True)
)