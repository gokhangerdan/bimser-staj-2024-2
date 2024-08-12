from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.dependencies.upload_documents import load_documents_and_upload, query_documents_in_qdrant

app = FastAPI()

class Query(BaseModel):
    query_text: str
    top_k: int = 5

#Bu endpoint, belirlenen klasördeki tüm dokümanları Qdrant'a yükler.
@app.post("/insert_document/")
def insert_document():
    try:
        load_documents_and_upload()  # Dokümanları yükle
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Bu endpoint, verilen sorgu metnini embedding'e çevirir ve Qdrant'ta arama yapar.
@app.post("/query_documents/")
def query_documents(query: Query):
    try:
        results = query_documents_in_qdrant(query.query_text, query.top_k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
