import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

# Initialize Spotipy client


def init_spotify():
    """
    Initialize Spotify client with OAuth credentials.
    Returns: Spotipy client object
    """
    scope = "user-read-playback-state user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope
    ))
    return sp


def get_current_track(sp):
    """
    Fetch current track info from Spotify.
    Returns: dict with keys: 'name', 'artist', 'album_cover'
    """
    try:
        current = sp.current_playback()
        if current and current['item']:
            track_name = current['item']['name']
            artist_name = current['item']['artists'][0]['name']
            # largest cover
            album_cover = current['item']['album']['images'][0]['url']
            return {
                'name': track_name,
                'artist': artist_name,
                'album_cover': album_cover
            }
        else:
            return {
                'name': 'No track playing',
                'artist': '',
                'album_cover': None
            }
    except Exception as e:
        print(f"[Spotify Utils] Error fetching current track: {e}")
        return {
            'name': 'Error',
            'artist': '',
            'album_cover': None
        }


def play(sp):
    """Resume playback on active Spotify device"""
    try:
        sp.start_playback()
    except Exception as e:
        print(f"[Spotify Utils] Error on play: {e}")


def pause(sp):
    """Pause playback on active Spotify device"""
    try:
        sp.pause_playback()
    except Exception as e:
        print(f"[Spotify Utils] Error on pause: {e}")


def next_track(sp):
    """Skip to next track on active Spotify device"""
    try:
        sp.next_track()
    except Exception as e:
        print(f"[Spotify Utils] Error on next track: {e}")
