import numpy as np

from ..dependencies.create_embeddings import create_embedding


def test_create_embedding():
    text = ["This is an example sentence"]
    
    embedding = create_embedding(text)

    assert isinstance(embedding, np.ndarray)
    assert len(embedding)==1
    assert isinstance(embedding[0], np.ndarray)
    assert len(embedding[0])==1024
    assert isinstance(embedding[0][0], np.float32)
    
def test_create_embedding_multiple():
    text = ["This is an example sentence", "This is another example sentence"]
    
    embedding = create_embedding(text)

    assert isinstance(embedding, np.ndarray)
    assert len(embedding)==2
    assert isinstance(embedding[0], np.ndarray)
    assert len(embedding[0])==1024
    assert isinstance(embedding[0][0], np.float32)
