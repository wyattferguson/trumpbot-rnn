from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import os


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, batch_input_shape=[batch_size, None]),
        tf.keras.layers.LSTM(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model


def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)


def parse_training_file():
    training_file = './tweets.txt'

    text = open(training_file, 'rb').read().decode(encoding='utf-8')
    vocab = sorted(set(text))
    char2idx = {u:i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)
    text_as_int = np.array([char2idx[c] for c in text])
    return [len(vocab), char2idx, idx2char, text_as_int]


def model_train():
    EPOCHS = 50
    BATCH_SIZE = 64
    BUFFER_SIZE = 10000
    EMBEDDING_DIM = 256
    RNN_UNITS = 1024
    SEQ_LENGTH = 140

    vocab_len, __, __, text_as_int = parse_training_file()

    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
    sequences = char_dataset.batch(SEQ_LENGTH+1, drop_remainder=True)

    dataset = sequences.map(split_input_target)
    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

    model = build_model(
        vocab_size = vocab_len,
        embedding_dim=EMBEDDING_DIM,
        rnn_units=RNN_UNITS,
        batch_size=BATCH_SIZE)

    model.compile(optimizer='adam', loss=loss)
    
    checkpoint_prefix = os.path.join('./training_checkpoints', "ckpt_{epoch}")

    checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_prefix,
        save_weights_only=True)

    history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
    return history


if __name__ == "__main__":
    model_train()