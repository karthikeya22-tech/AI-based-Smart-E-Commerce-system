# Embedding generation service
from pathlib import Path

import numpy as np
import pandas as pd


class EmbeddingService:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parents[2]

        self.embedding_path = BASE_DIR / "data" / "clip_embeddings.npy"
        self.metadata_path = BASE_DIR / "data" / "metadata.csv"

        self.embeddings = np.load(self.embedding_path)

        self.metadata = pd.read_csv(self.metadata_path)

        self.metadata.reset_index(drop=True, inplace=True)

        print("Embeddings Loaded:", self.embeddings.shape)
        print("Metadata Loaded:", self.metadata.shape)

    def get_embeddings(self):

        return self.embeddings

    def get_metadata(self):

        return self.metadata

    def get_product(self, index: int):

        return self.metadata.iloc[index]

    def get_product_by_id(self, product_id: int):

        result = self.metadata[
            self.metadata["id"] == product_id
        ]

        if result.empty:
            return None

        return result.iloc[0]

    def get_index(self, product_id: int):

        result = self.metadata[
            self.metadata["id"] == product_id
        ]

        if result.empty:
            return None

        return result.index[0]

    def get_embedding(self, index: int):

        return self.embeddings[index]


embedding_service = EmbeddingService()