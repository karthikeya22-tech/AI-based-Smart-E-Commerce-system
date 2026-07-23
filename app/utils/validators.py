from typing import Any, Dict


def validate_pagination(page: int, limit: int) -> Dict[str, int]:
    """Normalize pagination values for route handlers."""
    normalized_page = max(page, 1)
    normalized_limit = max(min(limit, 100), 1)
    return {
        "page": normalized_page,
        "limit": normalized_limit,
        "offset": (normalized_page - 1) * normalized_limit,
    }


def ensure_non_empty(value: Any, field_name: str) -> None:
    """Raise a ValueError if a required field is empty."""
    if value in (None, ""):
        raise ValueError(f"{field_name} is required")
