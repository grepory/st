from pydantic import BaseModel


class LinkMapping(BaseModel):
    slug: str
    url: str
