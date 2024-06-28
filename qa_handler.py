# summarizer/qa_handler.py
from sentence_transformers import SentenceTransformer
from .vector_db import VectorDB
import numpy as np

# Initialize SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize VectorDB with the correct dimension size (e.g., 384 for 'all-MiniLM-L6-v2')
vector_db = VectorDB(dimension=384)

def preprocess_text(text):
    # Add your preprocessing steps here
    return text

def get_vector(text):
    preprocessed_text = preprocess_text(text)
    vector = model.encode(preprocessed_text)
    return vector

def add_qa_pairs_to_db(qa_pairs):
    vectors = [get_vector(pair['question']) for pair in qa_pairs]
    vector_db.add_vectors(np.array(vectors))

def get_closest_answer(query):
    query_vector = get_vector(query).reshape(1, -1)
    indices, distances = vector_db.search(query_vector)
    # Fetch the closest answer based on indices
    return indices[0]  # Update to fetch actual answer from your DB
