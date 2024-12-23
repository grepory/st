import os

from atproto import Client

from app.core.config import settings
from app.crud import get_link, associate_bsky_uri
from app.celery import celery


client = Client()
client.login(settings.bsky_username, settings.bsky_password)

@celery.task(
    bind=True,
    max_retries=10,
    default_retry_delay=30,
)
async def bsky_post(self, slug: str):
    try:
        result = await get_link(slug)
        post = client.send_post(result['url'])
        await associate_bsky_uri(slug, post.uri)
    except Exception as e:
        print(f"Task failed: {e}. Retrying...")
        raise self.retry(e=e)