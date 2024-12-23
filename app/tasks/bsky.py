import os

from atproto import Client

from app.core.config import settings
from app.crud import get_link
from app.celery import celery


client = Client()
client.login(settings.bsky_username, settings.bsky_password)

@celery.task
async def bsky_post(slug: str):
    result = await get_link(slug)

    client.send_post(result['url'])