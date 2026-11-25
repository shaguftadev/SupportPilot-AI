from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_health():
    response=client.get("/health")
    assert response.status_code==200
    assert response.json()["status"]=="ok"

def test_readiness():
    response=client.get("/ready")
    assert response.status_code==200
    assert response.json()["database"]=="connected"

def test_ticket_list():
    response=client.get("/api/tickets")
    assert response.status_code==200
    assert isinstance(response.json(),list)
