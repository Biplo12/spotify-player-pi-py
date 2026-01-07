# Raspberry Pi Date Display

A simple Python application that displays the current date and time in ASCII art format. Designed to work via SSH without requiring X server or GUI libraries.

## Features

- ASCII art display with box borders
- Real-time date and time updates
- No X server or GUI required - works in terminal
- Can be run via SSH
- Simple or boxed display modes
- Configurable update interval

## Requirements

- Python 3.x (uses only standard library)
- Terminal access (SSH or direct)
- No X server or GUI libraries needed!

## Installation

1. Transfer the files to your Raspberry Pi:

   ```bash
   scp main.py pi@your-pi-ip:/home/pi/spotify-player-pi-py/
   ```

2. SSH into your Raspberry Pi:

   ```bash
   ssh pi@your-pi-ip
   ```

## Usage

### Basic Usage (Boxed Display)

```bash
python3 main.py
```

### Simple Text Mode

```bash
python3 main.py --simple
```

### Custom Update Interval

```bash
python3 main.py --interval 5
```

This updates every 5 seconds instead of every second.

### Exit

Press `Ctrl+C` to exit

## Command Line Options

- `--interval N`: Update interval in seconds (default: 1)
- `--simple`: Use simple text format without boxes
- `-h, --help`: Show help message

## Display Example

```
╔═══════════════════════════════╗
║   RASPBERRY PI CLOCK          ║
╚═══════════════════════════════╝

╔══════════════════════════╗
║        Monday            ║
╚══════════════════════════╝

╔══════════════════════════╗
║   January 15, 2024       ║
╚══════════════════════════╝

╔════════════════════════════╗
║      03:45:30 PM          ║
╚════════════════════════════╝
```

## Notes

- No X server or DISPLAY environment variable needed
- Works perfectly via SSH
- Updates automatically every second (configurable)
- Clears screen on each update for clean display

## Running on Startup

To run automatically on boot, you can:

1. Add to `.bashrc` or `.profile` for autostart on login
2. Create a systemd service
3. Add to `/etc/rc.local` for boot-time execution

Example systemd service (`/etc/systemd/system/date-display.service`):

```ini
[Unit]
Description=Date Display Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/spotify-player-pi-py
ExecStart=/usr/bin/python3 /home/pi/spotify-player-pi-py/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then enable it:

```bash
sudo systemctl enable date-display.service
sudo systemctl start date-display.service
```
