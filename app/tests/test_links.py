from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_link():
    response = client.post("/links/", json={"slug": "example", "url": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Mapping created successfully"

    response = client.get("/links/example")
    assert response.status_code == 200
