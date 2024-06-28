import re
from nltk.tokenize import sent_tokenize

def preprocess_text(text):
    # Remove special characters and extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    return sentences
