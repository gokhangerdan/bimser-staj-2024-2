from ..dependencies.create_embeddings import create_embedding


def test_create_embedding():
    text1 = "This is an example sentence"
    text2 = "This is another sentence"
    
    embedding1 = create_embedding(text1)
    embedding2 = create_embedding(text2)
    
    
    assert embedding1 != embedding2
    
   