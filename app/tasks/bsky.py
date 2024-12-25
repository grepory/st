from atproto import Client
from atproto_client.utils import TextBuilder

from app.core.config import settings
from app.crud import associate_bsky_uri

async def bsky_post(slug: str):
    client = Client()
    client.login(settings.bsky_username, settings.bsky_password)
    uri = f"{settings.base_uri}/{slug}"
    tb = TextBuilder()
    tb.link(uri, uri)
    post = client.send_post(tb)
    await associate_bsky_uri(slug, post.uri)