from fastembed import TextEmbedding
import numpy as np

# Embedding modeli yükle
embedding_model = TextEmbedding(model_name="intfloat/multilingual-e5-large")

# Bu fonksiyon, verilen metni embedding (vektör) formatına çevirir.
def create_embedding(documents: list):
    embeddings_list = list(embedding_model.embed(documents))
    embeddings = np.asarray(embeddings_list)
    return embeddings

if __name__ == '__main__':
    documents = ["This is an example sentence"]  # Bu bir örnek cümle
    embeddings = create_embedding(documents)  # Her metin için ayrı embedding oluştur
    print(embeddings)
