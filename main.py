#!/usr/bin/env python3
"""
Raspberry Pi Date Display
Displays current date and time in ASCII art format.
Can be run via SSH - no X server required!
"""

import os
import sys
import time
from datetime import datetime


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def create_box_border(text, width=None):
    """Create a box border around text"""
    if width is None:
        width = len(text) + 4
    top_bottom = '═' * (width - 2)
    border = f'╔{top_bottom}╗\n║ {text.center(width - 4)} ║\n╚{top_bottom}╝'
    return border


def format_date_time():
    """Format current date and time"""
    now = datetime.now()

    day_name = now.strftime('%A')
    date_str = now.strftime('%B %d, %Y')
    time_str = now.strftime('%I:%M:%S %p')

    return day_name, date_str, time_str


def display_ascii_clock():
    """Display date and time in ASCII art format"""
    clear_screen()

    day_name, date_str, time_str = format_date_time()

    # Calculate widths for consistent box sizes
    max_width = max(len(day_name), len(date_str), len(time_str)) + 4

    # Print header
    print('\n' + '═' * (max_width + 2))
    print(' ' * ((max_width - 22) // 2) + 'RASPBERRY PI CLOCK')
    print('═' * (max_width + 2) + '\n')

    # Day of week
    print(create_box_border(day_name, max_width))
    print()

    # Date
    print(create_box_border(date_str, max_width))
    print()

    # Time (larger)
    time_box = create_box_border(time_str, max_width + 2)
    print(time_box)

    # Footer
    print('\n' + '─' * (max_width + 2))
    print(' ' * ((max_width - 10) // 2) + 'Press Ctrl+C to exit')
    print('─' * (max_width + 2) + '\n')


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Display date and time in ASCII format on Raspberry Pi'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=1,
        help='Update interval in seconds (default: 1)'
    )
    parser.add_argument(
        '--simple',
        action='store_true',
        help='Use simple text format without boxes'
    )
    args = parser.parse_args()

    try:
        while True:
            if args.simple:
                clear_screen()
                day_name, date_str, time_str = format_date_time()
                print('\n' + '=' * 50)
                print(f'  {day_name}')
                print(f'  {date_str}')
                print(f'  {time_str}')
                print('=' * 50)
                print('\nPress Ctrl+C to exit\n')
            else:
                display_ascii_clock()

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
