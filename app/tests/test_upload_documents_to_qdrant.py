from ..dependencies.upload_documents import upload_documents_to_qdrant
import pytest


@pytest.fixture
def mock_create_embedding(monkeypatch):
    def mock_embedding_function(text):
        return [0.1, 0.2, 0.3]  # Sabit bir embedding döndür
    monkeypatch.setattr("..dependencies.upload_documents.create_embedding", mock_embedding_function)  # Fonksiyonu mockla

@pytest.fixture
def mock_qdrant_client(monkeypatch):
    class MockQdrantClient:
        def upsert(self, collection_name, points):
            assert collection_name == "my_collection"
            assert len(points) == 1
            assert points[0]['vector'] == [0.1, 0.2, 0.3]
            assert points[0]['payload']["path"] == "test_path/test.md"
            assert points[0]['payload']["content"] == "Test content"
    monkeypatch.setattr("..dependencies.upload_documents.qdrant_client", MockQdrantClient())  # qdrant_client'ı mockla

def test_upload_documents_to_qdrant_success(mock_qdrant_client, mock_create_embedding):
    documents = [
        {"path": "test_path/test.md", "content": "Test content"}
    ]
    res = upload_documents_to_qdrant(documents)  # Mock'lanmış fonksiyonları kullanarak yükleme yap
    assert res == 1
 

