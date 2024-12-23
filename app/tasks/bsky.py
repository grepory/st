from atproto import Client
from atproto_client.utils import TextBuilder

from app.core.config import settings
from app.crud import associate_bsky_uri
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
        uri = f"{settings.base_uri}/{slug}"
        tb = TextBuilder()
        tb.link(uri, uri)
        post = client.send_post(tb)
        await associate_bsky_uri(slug, post.uri)
    except Exception as e:
        print(f"Task failed: {e}. Retrying...")
        raise self.retry(e=e)