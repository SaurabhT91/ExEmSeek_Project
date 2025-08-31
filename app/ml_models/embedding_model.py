from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import layers, models

vocab_size = 1000
max_len = 20
embed_dim = 16

tokenizer = Tokenizer(num_words=vocab_size)

def build_embedding_model():
    model = models.Sequential([
        layers.Embedding(input_dim=vocab_size, output_dim=embed_dim, input_length=max_len),
        layers.GlobalAveragePooling1D(),
    ])
    return model

model = build_embedding_model()

def train_tokenizer(texts: list[str]):
    tokenizer.fit_on_texts(texts)

def texts_to_padded_sequences(texts: list[str]):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=max_len, padding='post')
    return padded

def get_embeddings(texts: list[str]):
    padded = texts_to_padded_sequences(texts)
    embeddings = model.predict(padded)
    return embeddings
