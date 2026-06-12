# app/ai_models/gru_model.py

import tensorflow as tf
from tensorflow.keras import layers


def build_gru(input_dim):

    model = tf.keras.Sequential([
        layers.Reshape((input_dim, 1), input_shape=(input_dim,)),
        layers.GRU(64),
        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model