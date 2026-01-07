#!/bin/bash

echo "Testing clock setup..."
echo ""

# Check if script exists
if [ -f "$(dirname "$0")/start_clock.sh" ]; then
    echo "✓ start_clock.sh exists"
else
    echo "✗ start_clock.sh not found"
    exit 1
fi

# Check if main script exists
if [ -f "$(dirname "$0")/spotify_player.py" ]; then
    echo "✓ spotify_player.py exists"
else
    echo "✗ spotify_player.py not found"
    exit 1
fi

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✓ Python 3 is installed"
    python3 --version
else
    echo "✗ Python 3 not found"
    exit 1
fi

# Check if tkinter is available
python3 -c "import tkinter" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ tkinter is installed"
else
    echo "✗ tkinter not found - install with: sudo apt-get install python3-tk"
    exit 1
fi

# Check display
echo ""
echo "Display check:"
echo "DISPLAY=${DISPLAY:-not set}"

# Check crontab
echo ""
echo "Crontab entries for this script:"
crontab -l 2>/dev/null | grep "start_clock.sh" || echo "No crontab entry found"

echo ""
echo "Setup check complete!"
echo ""
echo "To test the clock manually, run:"
echo "  /home/pi/spotify-player-pi-py/start_clock.sh"
echo ""
echo "To test auto-start, reboot:"
echo "  sudo reboot"
