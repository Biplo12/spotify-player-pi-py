import PySimpleGUI as sg
import time
from utils.spotify_utils import init_spotify, get_current_track, play, pause, next_track
from config import SCREEN_WIDTH, SCREEN_HEIGHT, UPDATE_INTERVAL

# -----------------------------
# Initialize Spotify Client
# -----------------------------
sp = init_spotify()

# -----------------------------
# PySimpleGUI Layout
# -----------------------------
sg.theme('DarkBlue3')

layout = [
    [sg.Text('', size=(20, 2), key='-TITLE-', justification='center')],
    [sg.Text('', size=(20, 1), key='-ARTIST-', justification='center')],
    [sg.Button('Play', size=(8, 2)), sg.Button(
        'Pause', size=(8, 2)), sg.Button('Next', size=(8, 2))]
]

window = sg.Window(
    'Spotify TFT Player',
    layout,
    size=(SCREEN_WIDTH, SCREEN_HEIGHT),
    finalize=True,
    no_titlebar=True,
    grab_anywhere=True
)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    event, values = window.read(timeout=UPDATE_INTERVAL * 1000)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Play':
        play(sp)
    elif event == 'Pause':
        pause(sp)
    elif event == 'Next':
        next_track(sp)

    track = get_current_track(sp)
    window['-TITLE-'].update(track['name'])
    window['-ARTIST-'].update(track['artist'])

# -----------------------------
# Close Window
# -----------------------------
window.close()
