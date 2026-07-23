import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def cosine_similarity_matrix(query_embedding: np.ndarray, embeddings: np.ndarray) -> np.ndarray:
    """Compute cosine similarity between a query embedding and a matrix."""
    return cosine_similarity([query_embedding], embeddings)[0]
