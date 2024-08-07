from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from typing import List
import os
import glob
import logging
import uuid

app = FastAPI()

# Qdrant Client kurulumu
qdrant_client = QdrantClient("http://localhost:6333")

# Embedding modeli
model = SentenceTransformer('all-MiniLM-L6-v2')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_embedding(text: str) -> List[float]:
    embedding = model.encode(text).tolist()
    logger.info(f"Generated embedding for text: {embedding[:5]}...")  # İlk 5 değeri göster
    return embedding

def read_markdown_files(directory):
    file_contents = []
    for filepath in glob.glob(os.path.join(directory, '**/*.md'), recursive=True):
        if os.path.isfile(filepath):  # Dosya yolunun gerçekten bir dosya olup olmadığını kontrol et
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                file_contents.append({"path": filepath, "content": content})
    return file_contents

def load_documents_to_qdrant(directory):
    documents = read_markdown_files(directory)
    for doc in documents:
        try:
            embedding = get_embedding(doc['content'])
            doc_id = str(uuid.uuid4())  # UUID olarak ID oluştur
            qdrant_client.upsert(
                collection_name="my_collection",
                points=[
                    {
                        "id": doc_id,
                        "vector": embedding,
                        "payload": {"content": doc['content']}
                    }
                ]
            )
            logger.info(f"Loaded document {doc['path']} with embedding {embedding[:5]}...")  # İlk 5 değeri göster
        except Exception as e:
            logger.error(f"Error loading document {doc['path']}: {e}")
            raise HTTPException(status_code=500, detail=f"Error loading document {doc['path']}: {e}")

class Document(BaseModel):
    id: str
    content: str
    embedding: List[float]

class Query(BaseModel):
    query_text: str
    top_k: int

@app.post("/insert_document/")
async def insert_document(doc: Document):
    try:
        embedding = get_embedding(doc.content)
        doc_id = str(uuid.uuid4())  # UUID olarak ID oluştur
        response = qdrant_client.upsert(
            collection_name="my_collection",
            points=[
                {
                    "id": doc_id,
                    "vector": embedding,
                    "payload": {"content": doc.content}
                }
            ]
        )
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error inserting document {doc.id}: {e}")
        raise HTTPException(status_code=500, detail=f"Error inserting document {doc.id}: {e}")

@app.post("/query_documents/")
async def query_documents(query: Query):
    try:
        query_vector = get_embedding(query.query_text)
        results = qdrant_client.search(
            collection_name="my_collection",
            query_vector=query_vector,
            limit=query.top_k
        )
        return results
    except Exception as e:
        logger.error(f"Error querying documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error querying documents: {e}")

@app.post("/load_documents/")
async def load_documents():
    try:
        directory = './docs'
        load_documents_to_qdrant(directory)
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error loading documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error loading documents: {e}")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup_event():
    try:
        qdrant_client.recreate_collection(
            collection_name="my_collection",
            vectors_config={
                "size": 384,  # Embedding boyutu
                "distance": "Cosine"  # Mesafe ölçütü
            }
        )
    except Exception as e:
        logger.error(f"Error recreating collection: {e}")
        raise HTTPException(status_code=500, detail=f"Error recreating collection: {e}")
