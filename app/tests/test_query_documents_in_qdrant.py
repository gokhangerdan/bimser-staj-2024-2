from ..dependencies.upload_documents import query_documents_in_qdrant


def test_query_documents_in_qdrant():
    results = query_documents_in_qdrant("python", 3)
    assert len(results) == 3

def test_not_found_query():
    results = query_documents_in_qdrant("nonexistent_word", 5)
    assert len(results) == 0