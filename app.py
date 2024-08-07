from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

stored_vectors = []

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        content = await file.read()
        print(f"File content (raw bytes): {content}")  # Dosyanın ham byte içeriği
        try:
            decoded_content = content.decode('utf-8')
            print(f"File content (decoded): {decoded_content}")  # Dosyanın decode edilmiş hali
            vector = convert_to_vector(decoded_content)
            print(f"Vector: {vector}")  # ASCII değerlerine dönüştürülen vektör
            stored_vectors.append({"filename": file.filename, "vector": vector})
        except UnicodeDecodeError as e:
            print(f"Decoding error: {e}")
            stored_vectors.append({"filename": file.filename, "vector": []})
    return {"message": "Files uploaded successfully"}

@app.get("/vectors/")
async def get_vectors():
    return {"vectors": stored_vectors}

def convert_to_vector(content):
    # İçeriği ASCII değerlerine dönüştürüyoruz.
    return [ord(char) for char in content]

# Bu dosyayı çalıştırmak için terminalde aşağıdaki komutu kullanın:
# uvicorn app:app --reload --port 8001
