import io
import urllib.request
from urllib.parse import urlparse

import PIL.Image


def is_url(path: str) -> bool:
    """Check if a path is a URL (http or https)."""
    try:
        result = urlparse(path)
        return result.scheme in ("http", "https")
    except Exception:
        return False


def download_image_from_url(url: str) -> bytes | None:
    """Download image data from a URL.
    
    Args:
        url: The URL to download the image from
        
    Returns:
        Image data as bytes, or None if download fails
    """
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return response.read()
    except Exception as e:
        from loguru import logger
        logger.error(f"Failed to download image from URL: {url}, error: {e}")
        return None
