from pathlib import Path
from typing import Optional

from app.core.constants import SUPPORTED_IMAGE_EXTENSIONS


def resolve_image_path(image_path: Optional[str], base_dir: Optional[Path] = None) -> Optional[Path]:
    """Resolve a relative image path into a filesystem path when possible."""
    if not image_path:
        return None

    candidate = Path(image_path)
    if candidate.is_absolute():
        return candidate

    if base_dir is not None:
        return base_dir / candidate

    return candidate


def is_supported_image_extension(path: str) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
