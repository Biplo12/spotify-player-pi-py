import os
from typing import Optional
from urllib.request import urlopen


def download_album_cover(url: Optional[str], save_path: str) -> bool:
    """
    Download an image from URL to save_path. Returns True on success.
    """
    if not url:
        return False

    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with urlopen(url, timeout=10) as response, open(save_path, "wb") as out:
            out.write(response.read())
        return True
    except Exception:
        return False
