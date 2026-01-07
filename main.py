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


def create_box_border(text, width=None, height=3):
    """Create a larger box border around text"""
    if width is None:
        width = len(text) + 8
    top_bottom = '═' * (width - 2)
    border_lines = [f'╔{top_bottom}╗']

    # Calculate number of empty rows before and after text
    empty_rows = height - 3  # total - top - text - bottom
    rows_before = empty_rows // 2
    rows_after = empty_rows - rows_before

    # Add empty rows before text
    for _ in range(rows_before):
        border_lines.append(f'║{" " * (width - 2)}║')

    # Add text row (centered)
    text_padding = (width - len(text) - 2) // 2
    text_row = f'║{" " * text_padding}{text}{" " * (width - len(text) - 2 - text_padding)}║'
    border_lines.append(text_row)

    # Add empty rows after text
    for _ in range(rows_after):
        border_lines.append(f'║{" " * (width - 2)}║')

    border_lines.append(f'╚{top_bottom}╝')
    return '\n'.join(border_lines)


def format_date_time():
    """Format current date and time"""
    now = datetime.now()

    day_name = now.strftime('%A')
    date_str = now.strftime('%B %d, %Y')
    time_str = now.strftime('%I:%M:%S %p')

    return day_name, date_str, time_str


def display_ascii_clock():
    """Display date and time in ASCII art format - optimized for 480x320 screen"""
    clear_screen()

    day_name, date_str, time_str = format_date_time()

    # Calculate widths for screen (target ~60-70 chars wide for 480px)
    max_width = 65
    time_width = 70

    # Add vertical padding to fill screen (320px = ~20-25 lines typical)
    print('\n' * 2)

    # Print header
    header_line = '═' * (max_width + 2)
    print(' ' * ((max_width - 22) // 2) + 'RASPBERRY PI CLOCK')
    print(header_line)
    print('\n' * 2)

    # Day of week - larger box
    print(create_box_border(day_name, max_width, height=5))
    print('\n' * 2)

    # Date - larger box
    print(create_box_border(date_str, max_width, height=5))
    print('\n' * 2)

    # Time - even larger box (main focus)
    print(create_box_border(time_str, time_width, height=7))

    # Footer padding
    print('\n' * 3)


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
                print('\n' * 3)
                print('=' * 65)
                print()
                print(' ' * 15 + day_name)
                print()
                print(' ' * 10 + date_str)
                print()
                print(' ' * 15 + time_str)
                print()
                print('=' * 65)
                print('\n' * 5)
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
