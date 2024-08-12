from sentence_transformers import SentenceTransformer

# Embedding modeli yükle
model = SentenceTransformer('all-MiniLM-L6-v2')

# Bu fonksiyon, verilen metni embedding (vektör) formatına çevirir.
def create_embedding(text: str):
    embedding = model.encode(text).tolist()  
    return embedding

if __name__ == '__main__':
    documents = ["This is an example sentence"]  # Bu bir örnek cümle
    embeddings = [create_embedding(doc) for doc in documents]  # Her metin için ayrı embedding oluştur
    print(embeddings)
