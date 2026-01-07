# Raspberry Pi Date Display

A simple Python application that displays the current date and time on your Raspberry Pi's desktop display. Designed to work with a 3.5" screen and can be run via SSH.

## Features

- Fullscreen or windowed mode
- Large, readable fonts optimized for small screens
- Real-time date and time updates
- Colored display (green date, cyan time)
- Can be run via SSH and will display on the Pi's connected screen

## Requirements

- Python 3.x (tkinter should be included by default)
- Raspberry Pi with a connected display (3.5" screen or HDMI)
- X server running on the Pi (for GUI display)

## Installation

1. Transfer the files to your Raspberry Pi:
   ```bash
   scp main.py pi@your-pi-ip:/home/pi/date-display/
   ```

2. SSH into your Raspberry Pi:
   ```bash
   ssh pi@your-pi-ip
   ```

## Usage

### Basic Usage (Fullscreen)

```bash
export DISPLAY=:0.0
python3 main.py
```

### Windowed Mode

```bash
export DISPLAY=:0.0
python3 main.py --windowed
```

### Exit

- Press `ESC` key to exit (in windowed mode)
- Or use `Ctrl+C` in the terminal

## Notes

- The `DISPLAY=:0.0` environment variable tells the script which display to use (the Pi's desktop)
- If you get permission errors, you may need to allow X11 forwarding or run with appropriate permissions
- The script automatically sets `DISPLAY=:0.0` if not already set, but it's good practice to export it manually

## Troubleshooting

**Error: "no display name and no $DISPLAY environment variable"**
- Make sure to export `DISPLAY=:0.0` before running the script
- Ensure X server is running on the Pi (`startx` if needed)

**Window doesn't appear on screen**
- Check that the display is properly connected and powered
- Verify the display is active: `sudo tvservice -s`
- Try running `xhost +local:` to allow local connections

**Fonts appear too small/large**
- Edit the font sizes in `main.py` (lines with `font.Font`)
- Adjust window size in windowed mode by modifying the geometry

## Running on Startup

To run automatically on boot, add to `/etc/xdg/autostart/` or use a systemd service.
