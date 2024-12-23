from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.database import database
from app.routers import links, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(links.router)
app.include_router(health.router)
