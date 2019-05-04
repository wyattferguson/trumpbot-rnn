from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import random
import learn

def generate_text(model, start_string):
    vocab_len, char2idx, idx2char, __ = learn.parse_training_file()
    # Number of characters to generate
    num_generate = random.randint(70,160)

    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []

    # Low temperatures results in more predictable text.
    # Higher temperatures results in more surprising text.
    temperature = random.randint(5,30) / 100

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the word returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # We pass the predicted word as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))


def load_model():
    vocab_len, __, __, __ = learn.parse_training_file()
    embedding_dim = 256
    rnn_units = 1024

    model = learn.build_model(vocab_len, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint('./training_checkpoints'))
    model.build(tf.TensorShape([1, None]))
    return model


def verbal_magic(tweets=1):
    model = load_model()
    # Give the RNN a jumping off point
    talking_points = ['hillary', 'health', 'obama', 'news', 'friends', 'korea', 'election', 'russia', 'loser']
    
    for i in range(0,tweets):
        start_string = np.random.choice(talking_points)
        tweet = generate_text(model, start_string=start_string)
        print('\n', tweet)
        


if __name__ == "__main__":
    tweets = 10
    verbal_magic(tweets)
