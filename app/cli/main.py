import typer
from typing import Optional
from pathlib import Path
import os
import requests

from app.core.config import settings

app = typer.Typer(
    name="st",
    help=f"Shitpost CLI",
    add_completion=True,
)

@app.command(
    name="post",
    help="Post a new shitpost",
)
def post(slug: str, url: str):
    api_token = os.getenv("API_TOKEN")
    if not api_token:
        raise typer.BadParameter("API_TOKEN environment variable is not set")
    
    response = requests.post(
        f"{settings.base_uri}/api/v1/links",
        json={"slug": slug, "url": url},
        headers={"X-SHITPOST-TOKEN": api_token}
    )
    
    if response.status_code == 200:
        print(f"Successfully created link {slug} -> {url}")
    else:
        print(f"Error creating link: {response.status_code}")
        print(response.text) 

if __name__ == "__main__":
    app()