from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import LinkMapping
from app.crud import create_link, get_link

router = APIRouter(tags=["links"])


@router.post("/links/")
async def create_link_mapping(mapping: LinkMapping):
    try:
        await create_link(mapping.slug, mapping.url)
        return {"message": "Mapping created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{slug}")
async def redirect_link(slug: str):
    result = await get_link(slug)
    if result:
        return RedirectResponse(url=result["url"])
    else:
        raise HTTPException(status_code=404, detail="Slug not found")
