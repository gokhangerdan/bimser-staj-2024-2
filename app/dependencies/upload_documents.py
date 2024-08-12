import os
from qdrant_client import QdrantClient
import uuid
from .create_embeddings import create_embedding

qdrant_client = QdrantClient("http://localhost:6333")

def read_documents(root_dir="docs/Synergy/CSP/trouble_shooting"):
    result = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if (file.endswith(".md") or file.endswith(".mdx")) and file != "in_progress.md":
                file_path = os.path.join(subdir, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    result.append({"path": file_path, "content": content})
    return result

def upload_documents_to_qdrant(documents):
    for doc in documents:
        try:
            embedding = create_embedding(doc['content'])
            qdrant_client.upsert(
                collection_name="my_collection",
                points=[
                    {
                        "id": str(uuid.uuid4()), 
                        "vector": embedding,
                        "payload": {"path": doc['path'], "content": doc['content']}
                    }
                ]
            )
            print(f"Successfully uploaded: {doc['path']}")
        except Exception as e:
            print(f"Error uploading document {doc['path']}: {e}")

def load_documents_and_upload():
    documents = read_documents()
    upload_documents_to_qdrant(documents)

def query_documents_in_qdrant(query_text, top_k=5):
    try:
        query_embedding = create_embedding(query_text)
        results = qdrant_client.search(
            collection_name="my_collection",
            query_vector=query_embedding,
            limit=top_k
        )
        return results
    except Exception as e:
        print(f"Error querying documents: {e}")
        return []
