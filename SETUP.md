# Raspberry Pi Auto-Start Setup

This guide will help you set up the clock application to run automatically on your Raspberry Pi startup.

## Prerequisites

1. Make sure Python 3 and tkinter are installed:

   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-tk
   ```

2. Install required Python packages:
   ```bash
   pip3 install -r requirements.txt
   ```

## Option 1: Systemd Service (Recommended)

1. Copy the service file to systemd directory:

   ```bash
   sudo cp clock.service /etc/systemd/system/
   ```

2. **Edit the service file** to match your setup:

   ```bash
   sudo nano /etc/systemd/system/clock.service
   ```

   Update these paths if your project is in a different location:

   - `WorkingDirectory=/home/admin/spotify-player-pi-py` (change `admin` to your username if different)
   - `User=admin` (change to your username)
   - `ExecStart=/usr/bin/python3 /home/admin/spotify-player-pi-py/spotify_player.py` (update path)

3. Reload systemd and enable the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable clock.service
   sudo systemctl start clock.service
   ```

4. Check if it's running:

   ```bash
   sudo systemctl status clock.service
   ```

5. To stop the service:

   ```bash
   sudo systemctl stop clock.service
   ```

6. To disable auto-start:
   ```bash
   sudo systemctl disable clock.service
   ```

## Option 2: Autostart (Desktop Environment)

If you're using a desktop environment (like Raspberry Pi OS Desktop):

1. Create an autostart directory if it doesn't exist:

   ```bash
   mkdir -p ~/.config/autostart
   ```

2. Create a desktop entry file:

   ```bash
   nano ~/.config/autostart/clock.desktop
   ```

3. Add this content (adjust paths as needed):

   ```ini
   [Desktop Entry]
   Type=Application
   Name=Clock
   Exec=/usr/bin/python3 /home/admin/spotify-player-pi-py/spotify_player.py
   Path=/home/admin/spotify-player-pi-py
   ```

4. Make it executable:
   ```bash
   chmod +x ~/.config/autostart/clock.desktop
   ```

## Option 3: Manual Startup Script

1. Make the startup script executable:

   ```bash
   chmod +x start_clock.sh
   ```

2. Add to `.bashrc` or create a cron job for @reboot:

   ```bash
   crontab -e
   ```

   Add this line (adjust path):

   ```
   @reboot /home/admin/spotify-player-pi-py/start_clock.sh
   ```

## Troubleshooting

- If the clock doesn't appear, check the display variable:

  ```bash
  echo $DISPLAY
  ```

  Usually it's `:0` for the primary display.

- Check logs for systemd service:

  ```bash
  sudo journalctl -u clock.service -f
  ```

- Test manually first:

  ```bash
  export DISPLAY=:0
  python3 spotify_player.py
  ```

- If you need to kill the process:
  ```bash
  pkill -f spotify_player.py
  ```
