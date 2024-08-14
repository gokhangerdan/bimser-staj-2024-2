from fastapi.testclient import TestClient

from ..main import app


client = TestClient(app)

def test_insert_document():
    response = client.post("/insert_document/")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}