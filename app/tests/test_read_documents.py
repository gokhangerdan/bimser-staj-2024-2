from ..dependencies.upload_documents import read_documents


def test_read_documents():
    result = read_documents()
    assert isinstance(result, list)
    assert len(result) > 0
