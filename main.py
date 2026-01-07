#!/usr/bin/env python3
"""
Raspberry Pi Date Display
Displays current date and time in simple text format.
Can be run via SSH - no X server required!
"""

import os
import sys
import time
from datetime import datetime


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def format_date_time():
    """Format current date and time"""
    now = datetime.now()

    date_str = now.strftime('%B %d, %Y')
    time_str = now.strftime('%I:%M %p')

    return date_str, time_str


def display_clock():
    """Display date and time - optimized for 480x320 screen"""
    clear_screen()

    date_str, time_str = format_date_time()

    # Add vertical padding to fill screen
    print('\n' * 6)

    # Time - large and centered (main focus)
    print(' ' * 10 + time_str)
    print('\n' * 8)

    # Date - below the time
    print(' ' * 5 + date_str)

    # Footer padding
    print('\n' * 5)


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Display date and time on Raspberry Pi'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=1,
        help='Update interval in seconds (default: 1)'
    )
    args = parser.parse_args()

    try:
        while True:
            display_clock()
            time.sleep(args.interval)
    except KeyboardInterrupt:
        clear_screen()
        print('\nExiting... Goodbye!\n')
        sys.exit(0)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
