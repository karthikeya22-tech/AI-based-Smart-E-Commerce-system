# Shared dependencies
from typing import Optional

from fastapi import Depends, HTTPException, Query

from app.database import supabase


def get_supabase():
    """
    Returns the shared Supabase client.
    """
    return supabase


def pagination(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Common pagination dependency.
    """
    offset = (page - 1) * limit

    return {
        "page": page,
        "limit": limit,
        "offset": offset
    }


def get_current_user():
    """
    Placeholder for authentication.

    This will be replaced with JWT authentication
    using Supabase Auth later.
    """
    raise HTTPException(
        status_code=501,
        detail="Authentication not implemented yet."
    )