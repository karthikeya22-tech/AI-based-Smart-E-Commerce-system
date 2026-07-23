# Reverse image search engine
from sklearn.metrics.pairwise import cosine_similarity

from app.services.clip_model import clip_model
from app.services.embedding_service import embedding_service


class ReverseSearchEngine:

    def __init__(self):

        self.embeddings = embedding_service.get_embeddings()
        self.metadata = embedding_service.get_metadata()

    def search(
        self,
        query: str,
        top_k: int = 10
    ):

        text_embedding = clip_model.encode_text(query)

        similarity = cosine_similarity(
            [text_embedding],
            self.embeddings
        )[0]

        indices = similarity.argsort()[::-1][:top_k]

        results = []

        for idx in indices:

            product = self.metadata.iloc[idx]

            results.append({

                "id": int(product["id"]),

                "product_name": product["productDisplayName"],

                "category": product["masterCategory"],

                "article_type": product["articleType"],

                "gender": product["gender"],

                "image": f"data/images/{product['id']}.jpg",

                "similarity": float(similarity[idx])

            })

        return results


reverse_search_engine = ReverseSearchEngine()