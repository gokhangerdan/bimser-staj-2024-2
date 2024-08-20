import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


df = pd.read_json('app/dependencies/moderation_model/data.jsonl')

with open('app/dependencies/moderation_model/embeddings.npy', 'rb') as f:
    X = np.load(f)

y = df.label.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.15)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy}')

model.save('app/dependencies/moderation_model/moderation_model.keras')

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.savefig("app/dependencies/moderation_model/moderation_model.png")
