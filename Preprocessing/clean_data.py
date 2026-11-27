import pandas as pd
import re

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text 
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Tokenization
def tokenize_text(text):
    words = text.split()
    return words

# Stopword Removal
def remove_stopwords(text):
    words = tokenize_text(text)

    filtered_words = [
        word for word in words
        if word not in ENGLISH_STOP_WORDS
    ]

    return " ".join(filtered_words)
