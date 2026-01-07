#!/usr/bin/env python3
"""
Raspberry Pi Date Display
Displays current date and time on the Pi's desktop display.
Can be run via SSH - make sure to export DISPLAY=:0.0 before running.
"""

import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import font


class DateDisplay:
    def __init__(self, fullscreen: bool = True):
        # Set display environment variable if not already set
        if 'DISPLAY' not in os.environ:
            os.environ['DISPLAY'] = ':0.0'
        
        self.root = tk.Tk()
        self.fullscreen = fullscreen
        
        # Configure window
        if fullscreen:
            self.root.attributes('-fullscreen', True)
        else:
            # Default size for 3.5" screen (typically 480x320 or 480x800)
            self.root.geometry('480x320')
            self.root.resizable(False, False)
        
        self.root.configure(bg='black')
        self.root.title('Date & Time Display')
        
        # Make window always on top
        self.root.attributes('-topmost', True)
        
        # Center the window if not fullscreen
        if not fullscreen:
            self.center_window()
        
        # Configure fonts
        self.date_font = font.Font(family='Helvetica', size=36, weight='bold')
        self.time_font = font.Font(family='Helvetica', size=48, weight='bold')
        self.day_font = font.Font(family='Helvetica', size=24, weight='normal')
        
        # Create UI elements
        self.create_widgets()
        
        # Bind escape key to exit
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Start updating
        self.update_time()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create and configure UI widgets"""
        # Main container
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True, fill='both')
        
        # Day of week label
        self.day_label = tk.Label(
            main_frame,
            text='',
            font=self.day_font,
            fg='white',
            bg='black'
        )
        self.day_label.pack(pady=(20, 10))
        
        # Date label
        self.date_label = tk.Label(
            main_frame,
            text='',
            font=self.date_font,
            fg='#00ff00',
            bg='black'
        )
        self.date_label.pack(pady=10)
        
        # Time label
        self.time_label = tk.Label(
            main_frame,
            text='',
            font=self.time_font,
            fg='#00ffff',
            bg='black'
        )
        self.time_label.pack(pady=20)
        
        # Instruction label (only in non-fullscreen mode)
        if not self.fullscreen:
            instruction = tk.Label(
                main_frame,
                text='Press ESC to exit',
                font=font.Font(family='Helvetica', size=12),
                fg='gray',
                bg='black'
            )
            instruction.pack(side='bottom', pady=10)
    
    def update_time(self):
        """Update the displayed date and time"""
        now = datetime.now()
        
        # Format day of week
        day_name = now.strftime('%A')
        self.day_label.config(text=day_name)
        
        # Format date
        date_str = now.strftime('%B %d, %Y')
        self.date_label.config(text=date_str)
        
        # Format time
        time_str = now.strftime('%I:%M:%S %p')
        self.time_label.config(text=time_str)
        
        # Schedule next update in 1 second
        self.root.after(1000, self.update_time)
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print('\nExiting...')
            self.root.quit()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Display date and time on Raspberry Pi desktop'
    )
    parser.add_argument(
        '--windowed',
        action='store_true',
        help='Run in windowed mode instead of fullscreen'
    )
    args = parser.parse_args()
    
    try:
        app = DateDisplay(fullscreen=not args.windowed)
        app.run()
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        print('\nTip: If you get a display error, try running:')
        print('export DISPLAY=:0.0')
        print('before executing this script.')
        sys.exit(1)


if __name__ == '__main__':
    main()
