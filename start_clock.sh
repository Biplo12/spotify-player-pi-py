#!/bin/bash

# Wait for display to be ready
sleep 5

# Set display (adjust if needed, usually :0 for primary display)
export DISPLAY=:0

# Navigate to script directory
cd "$(dirname "$0")"

# Run the clock application
python3 spotify_player.py
