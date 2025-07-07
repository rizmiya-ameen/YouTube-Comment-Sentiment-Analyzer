import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

VOCAB_SIZE = 10000
MAX_LEN = 250
MODEL_PATH = 'sentiment_analysis_model.h5'

# Load the saved model
model = load_model(MODEL_PATH)

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def encode_texts(text_list):
    encoded_texts = []
    for text in text_list:
        tokens = tf.keras.preprocessing.text.text_to_word_sequence(text)
        token_indices = []
        for word in tokens:
            index = tokenizer.word_index.get(word, 0)
            # Check if index is within vocab size
            if index < VOCAB_SIZE:
                token_indices.append(index)
            else:
                token_indices.append(0)  # Replace out-of-vocab with 0
        encoded_texts.append(token_indices)
    return pad_sequences(encoded_texts, maxlen=MAX_LEN, padding='post', value=VOCAB_SIZE - 1)


def predict_sentiments(text_list):
    encoded_inputs = encode_texts(text_list)
    predictions = np.argmax(model.predict(encoded_inputs, verbose=0), axis=-1)
    sentiments = []
    for prediction in predictions:
        if prediction == 0:
            sentiments.append("Negative")
        elif prediction == 1:
            sentiments.append("Neutral")
        else:
            sentiments.append("Positive")
    return sentiments
