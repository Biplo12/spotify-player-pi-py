#!/bin/bash

# Wait for display to be ready
sleep 5

# Detect the display for the logged-in user
# Try to find who's logged into the graphical session
LOGIN_USER=$(who | grep '(:' | awk '{print $1}' | head -n1)

# If we found a logged-in user, try to get their display
if [ -n "$LOGIN_USER" ]; then
    DISPLAY_NUM=$(who | grep "$LOGIN_USER" | grep '(:' | awk '{print $5}' | sed 's/[()]//g' | head -n1)
    if [ -n "$DISPLAY_NUM" ]; then
        export DISPLAY="$DISPLAY_NUM"
    else
        export DISPLAY=:0
    fi
else
    # Fallback to default display
    export DISPLAY=:0
fi

# Alternative: Try to find display from X server
if [ ! -S "/tmp/.X11-unix/X0" ] && [ -S "/tmp/.X11-unix/X1" ]; then
    export DISPLAY=:1
fi

# Navigate to script directory
cd "$(dirname "$0")"

# Run the clock application
python3 spotify_player.py
