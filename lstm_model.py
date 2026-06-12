# app/ai_models/fnn_model.py

import tensorflow as tf
from tensorflow.keras import layers


def build_fnn(input_dim):

    model = tf.keras.Sequential([
        layers.Dense(128, activation="relu", input_shape=(input_dim,)),
        layers.Dense(64, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model