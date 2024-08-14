from fastapi.testclient import TestClient
from ..main import app



client = TestClient(app)



def test_query_documents():
    response = client.post("/query_documents/", json={"query_text": "example query", "top_k": 5})
    assert response.status_code == 200
    assert len(response.json()["results"]) == 5