# app/ai_models/cnn_lstm_model.py

import tensorflow as tf
from tensorflow.keras import layers


def build_cnn_lstm(input_dim):

    model = tf.keras.Sequential([
        layers.Reshape((input_dim, 1), input_shape=(input_dim,)),
        layers.Conv1D(32, 3, activation="relu"),
        layers.MaxPooling1D(),
        layers.LSTM(32),
        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model