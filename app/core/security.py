import hashlib
from typing import Dict


def hash_value(value: str) -> str:
    """Return a deterministic hash for sensitive identifiers."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def build_auth_header(token: str) -> Dict[str, str]:
    """Build a standard bearer token header."""
    return {"Authorization": f"Bearer {token}"}
