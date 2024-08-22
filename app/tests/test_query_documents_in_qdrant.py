from ..dependencies.upload_documents import query_documents_in_qdrant


def test_query_documents_in_qdrant():
    query_text = "test query"
    top_k = 3
    results = query_documents_in_qdrant(query_text, top_k)
    assert len(results) != 0

def test_not_found_query():
    results = query_documents_in_qdrant("nonexistent_word", 5)
    assert len(results) == 0
