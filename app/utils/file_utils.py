from pathlib import Path
from typing import Optional


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if it doesn't exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory
