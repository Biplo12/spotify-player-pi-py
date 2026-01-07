from typing import Optional
from PIL import Image, ImageTk


def update_track_info(title_label, artist_label, track_name: str, artist_name: str) -> None:
    """
    Update the Tkinter labels for track title and artist.
    """
    title_label.config(text=track_name or "")
    artist_label.config(text=artist_name or "")


def update_album_cover(image_label, image_path: str, width: int, height: int) -> None:
    """
    Load an image from disk, resize to (width, height), and set it on a Tkinter Label.
    Keeps a reference to avoid garbage collection.
    """
    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((max(1, width), max(1, height)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # keep reference
    except Exception:
        # If any error occurs, clear the image to avoid crashes
        image_label.config(image="")
        image_label.image = None
