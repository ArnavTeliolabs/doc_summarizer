# summarizer/vector_db.py
import faiss
import numpy as np

class VectorDB:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors):
        self.index.add(vectors)

    def search(self, query_vector, k=1):
        distances, indices = self.index.search(query_vector, k)
        return indices, distances
