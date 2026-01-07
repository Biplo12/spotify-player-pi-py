import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


def init_spotify():
    """
    Initialize and return a Spotify client using OAuth.
    """
    scope = "user-read-playback-state,user-modify-playback-state"
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def get_current_track(sp):
    """
    Get the current playing track information.
    Returns a dict with 'name', 'artist', and 'album_image_url'.
    """
    try:
        current = sp.current_playback()
        if current and current['is_playing']:
            track = current['item']
            if track:
                artists = ', '.join([artist['name']
                                    for artist in track['artists']])
                album_image = track['album']['images'][0]['url'] if track['album']['images'] else None
                return {
                    'name': track['name'],
                    'artist': artists,
                    'album_image_url': album_image
                }
    except Exception as e:
        print(f"Error getting current track: {e}")

    return {
        'name': 'No track playing',
        'artist': '',
        'album_image_url': None
    }


def play(sp):
    """Start playback on the user's active device."""
    try:
        sp.start_playback()
    except Exception as e:
        print(f"Error playing: {e}")


def pause(sp):
    """Pause playback on the user's active device."""
    try:
        sp.pause_playback()
    except Exception as e:
        print(f"Error pausing: {e}")


def next_track(sp):
    """Skip to the next track."""
    try:
        sp.next_track()
    except Exception as e:
        print(f"Error skipping track: {e}")

