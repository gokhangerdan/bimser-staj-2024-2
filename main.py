# https://fastapi.tiangolo.com/tutorial/
from fastapi import FastAPI
from pydantic import BaseModel

# https://github.com/qdrant/qdrant-client
# https://qdrant.tech/documentation/concepts/
from qdrant_client import QdrantClient


client = QdrantClient(":memory:")
app = FastAPI()


class Search(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/search/")
def create_item(data: Search):
    print(data)
    return "Search result"
