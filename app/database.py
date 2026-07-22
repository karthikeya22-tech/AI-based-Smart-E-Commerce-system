# Database connection setup
from supabase import Client, create_client
from app.config import settings


class Database:

    def __init__(self):
        self.client: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_ANON_KEY
        )

    def get_client(self) -> Client:
        return self.client


db = Database()

supabase = db.get_client()