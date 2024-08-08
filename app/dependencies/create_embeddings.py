from sentence_transformers import SentenceTransformer


def create_embeddings(documents):
    # https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(documents)
    return embeddings


if __name__ == '__main__':
    documents = ["This is an example sentence"]
    embeddings = create_embeddings(documents=documents)
    print(embeddings)
