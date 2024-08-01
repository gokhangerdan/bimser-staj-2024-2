from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence"]

# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
print(type(embeddings), type(embeddings[0]))
print(len(embeddings[0]))