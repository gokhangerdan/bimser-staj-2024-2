from fastembed import TextEmbedding

import pandas as pd
import numpy as np


def create_embeddings(documents):
    embedding_model = TextEmbedding(model_name="intfloat/multilingual-e5-large")
    embeddings_list = list(embedding_model.embed(documents))
    embeddings = np.asarray(embeddings_list)
    return embeddings

df = pd.read_json('app/dependencies/moderation_model/data.jsonl')

arr = create_embeddings(df.message.values)

with open('app/dependencies/moderation_model/embeddings.npy', 'wb') as f:
    np.save(f, arr)