from app.database import supabase


class ProductService:
    """Service wrapper for product queries."""

    def list_products(self, page: int, limit: int):
        offset = (page - 1) * limit
        response = (
            supabase.table("products")
            .select("*")
            .range(offset, offset + limit - 1)
            .execute()
        )
        return response.data

    def get_product(self, product_id: int):
        response = (
            supabase.table("products")
            .select("*")
            .eq("id", product_id)
            .execute()
        )
        if not response.data:
            return None
        return response.data[0]


product_service = ProductService()
