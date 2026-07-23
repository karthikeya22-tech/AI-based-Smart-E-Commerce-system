# Recommendation engine
from sklearn.metrics.pairwise import cosine_similarity

from app.services.embedding_service import embedding_service


class RecommendationEngine:

    def __init__(self):

        self.embeddings = embedding_service.get_embeddings()
        self.metadata = embedding_service.get_metadata()

    def recommend(
        self,
        product_id: int,
        top_k: int = 8
    ):

        index = embedding_service.get_index(product_id)

        if index is None:
            return []

        query_embedding = self.embeddings[index]

        similarity = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        sorted_indices = similarity.argsort()[::-1]

        recommendations = []

        query_product = self.metadata.iloc[index]

        for idx in sorted_indices:

            if idx == index:
                continue

            product = self.metadata.iloc[idx]

            # Same gender
            if product["gender"] != query_product["gender"]:
                continue

            # Same usage
            if product["usage"] != query_product["usage"]:
                continue

            recommendations.append({

                "id": int(product["id"]),

                "product_name": product["productDisplayName"],

                "category": product["masterCategory"],

                "article_type": product["articleType"],

                "image": f"data/images/{product['id']}.jpg",

                "similarity": float(similarity[idx])

            })

            if len(recommendations) == top_k:
                break

        return recommendations


recommendation_engine = RecommendationEngine()