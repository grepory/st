import traceback

from fastapi import APIRouter, HTTPException, Header, Depends
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.schemas import LinkMapping
from app.crud import create_link, get_link, associate_bsky_uri
from app.tasks.bsky import bsky_post

router = APIRouter(tags=["links"])

async def verify_token(x_shitpost_token: str = Header('X-SHITPOST-TOKEN')):
    if x_shitpost_token != settings.api_token:
        raise HTTPException(
            status_code=401,
            detail="Invalid API token",
        )

@router.post("/api/v1/links", dependencies=[Depends(verify_token)])
async def create_link_mapping(mapping: LinkMapping):
    try:
        await create_link(mapping.slug, mapping.url)
        await bsky_post(mapping.slug)
        return {"message": "Mapping created successfully"}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{slug}")
async def redirect_link(slug: str):
    result = await get_link(slug)
    if result:
        return RedirectResponse(url=result["url"])
    else:
        raise HTTPException(status_code=404, detail="Slug not found")
