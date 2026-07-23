from app.api.auth import auth_status


def test_auth_status_route():
    assert auth_status()["authentication"] == "Supabase Auth integration pending"
