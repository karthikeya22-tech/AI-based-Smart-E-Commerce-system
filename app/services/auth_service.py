class AuthService:
    """Thin service layer for authentication-related operations."""

    def get_status(self) -> dict:
        return {"authentication": "Supabase Auth integration pending"}


auth_service = AuthService()
