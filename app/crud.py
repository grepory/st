from sqlalchemy.sql import select
from app.models import link_mappings
from app.database import database


async def get_link(slug: str):
    query = select(link_mappings).where(link_mappings.c.slug == slug)
    return await database.fetch_one(query)


async def create_link(slug: str, url: str):
    query = link_mappings.insert().values(slug=slug, url=url)
    return await database.execute(query)
