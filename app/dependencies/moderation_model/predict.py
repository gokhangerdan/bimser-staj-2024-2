import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from fastembed import TextEmbedding

import tensorflow as tf

import numpy as np


model = tf.keras.models.load_model('app/dependencies/moderation_model/moderation_model.keras')

def create_embeddings(documents):
    embedding_model = TextEmbedding(model_name="intfloat/multilingual-e5-large")
    embeddings_list = list(embedding_model.embed(documents))
    embeddings = np.asarray(embeddings_list)
    return embeddings

def result_prediction(documents):
    predictions = model.predict(create_embeddings([documents]))
    return predictions

predictions = model.predict(create_embeddings(["Merhaba nasılsın?"]))
