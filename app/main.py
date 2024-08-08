# https://fastapi.tiangolo.com/tutorial/
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# https://github.com/qdrant/qdrant-client
# https://qdrant.tech/documentation/concepts/
from qdrant_client import QdrantClient

from .dependencies.upload_documents import upload_to_qdrant


# https://qdrant.tech/documentation/quickstart/
client = QdrantClient(":memory:")
app = FastAPI()


COLLECTION_NAME = "test_collection"
TOP_K = 3

class Document(BaseModel):
    content: str

class Query(BaseModel):
    query: str


def qdrant_upsert_call(document_embedding: list):
    print(document_embedding)
    return True

def qdrant_search_call(query_embedding: list):
    print(query_embedding)
    return True

def create_embedding(text: str):
    print(text)
    return True


@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.post("/insert_document/")
def insert_document(data: Document):
    document_embedding = create_embedding(text=data.content)
    is_success = qdrant_upsert_call(document_embedding=document_embedding)
    if is_success:
        return "Document upserted"
    else:
        raise HTTPException(status_code=400, detail="Insert document failed")

@app.post("/query_documents/")
def query_documents(data: Query):
    query_embedding = create_embedding(text=data.query)
    is_success = qdrant_search_call(query_embedding=query_embedding)
    if is_success:
        return "Document content"
    else:
        raise HTTPException(status_code=400, detail="Query documents failed")
