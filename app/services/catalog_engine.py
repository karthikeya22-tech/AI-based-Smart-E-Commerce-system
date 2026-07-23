# Catalog processing engine
from sklearn.metrics.pairwise import cosine_similarity

from app.services.embedding_service import embedding_service


class CatalogEngine:

    def __init__(self):

        self.embeddings = embedding_service.get_embeddings()
        self.metadata = embedding_service.get_metadata()

    def build_catalog(
        self,
        similarity_threshold: float = 0.90
    ):

        catalog = []
        visited = set()

        for i in range(len(self.metadata)):

            if i in visited:
                continue

            representative = self.metadata.iloc[i]

            representative_embedding = self.embeddings[i]

            similarities = cosine_similarity(
                [representative_embedding],
                self.embeddings
            )[0]

            group = []

            for j, score in enumerate(similarities):

                if j in visited:
                    continue

                candidate = self.metadata.iloc[j]

                if (
                    candidate["articleType"] == representative["articleType"]
                    and candidate["baseColour"] == representative["baseColour"]
                    and score >= similarity_threshold
                ):

                    group.append({

                        "id": int(candidate["id"]),
                        "product_name": candidate["productDisplayName"],
                        "image": f"data/images/{candidate['id']}.jpg",
                        "similarity": float(score)

                    })

                    visited.add(j)

            catalog.append({

                "catalog_name": f"{representative['baseColour']} {representative['articleType']}",

                "representative": {

                    "id": int(representative["id"]),
                    "product_name": representative["productDisplayName"],
                    "image": f"data/images/{representative['id']}.jpg"

                },

                "products": group

            })

        return catalog


catalog_engine = CatalogEngine()