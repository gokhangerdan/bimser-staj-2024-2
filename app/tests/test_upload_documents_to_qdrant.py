from ..dependencies.upload_documents import upload_documents_to_qdrant,read_documents

def test_upload_documents_to_qdrant():
    document = read_documents()
    res = upload_documents_to_qdrant(document)
    assert res == {"status": "success"}




    

