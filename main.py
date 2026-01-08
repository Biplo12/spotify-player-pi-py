#!/usr/bin/env python3
"""
Raspberry Pi Date Display
Displays current date and time in simple text format.
Can be run via SSH - no X server required!
"""

import os
import sys
import time
import shutil
from datetime import datetime


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def format_date_time():
    """Format current date and time"""
    now = datetime.now()

    date_str = now.strftime('%B %d, %Y')
    time_str = now.strftime('%I:%M:%S %p')

    return date_str, time_str


def make_big_text(text):
    """Make text 3x bigger using block characters - optimized for time display"""
    # ASCII art patterns for large characters (3 lines tall)
    big_chars = {
        '0': ['███', '█ █', '███'],
        '1': ['██ ', ' █ ', '███'],
        '2': ['███', ' ██', '███'],
        '3': ['███', ' ██', '███'],
        '4': ['█ █', '███', '  █'],
        '5': ['███', '██ ', '███'],
        '6': ['███', '██ ', '███'],
        '7': ['███', '  █', '  █'],
        '8': ['███', '███', '███'],
        '9': ['███', '███', '███'],
        ':': ['   ', ' █ ', '   '],
        ' ': ['   ', '   ', '   '],
        'A': [' █ ', '█ █', '███'],
        'P': ['███', '█ █', '█  '],
        'M': ['█ █', '███', '█ █'],
    }

    lines = ['', '', '']
    for char in text.upper():
        if char in big_chars:
            pattern = big_chars[char]
        else:
            # For unknown characters, use bold pattern
            pattern = [f'█{char}█', f' {char} ', f'█{char}█']

        for i in range(3):
            lines[i] += pattern[i] + ' '

    return '\n'.join(lines)


def display_clock():
    """Display date and time - optimized for 480x320 screen"""
    clear_screen()

    date_str, time_str = format_date_time()

    # Get terminal width for centering (480px screen ≈ 60 chars at 8px/char)
    try:
        terminal_size = shutil.get_terminal_size()
        screen_width = terminal_size.columns
    except (AttributeError, OSError):
        # Fallback for 480x320 screen: ~60 characters wide
        screen_width = 60

    # Create big text (3x larger)
    big_time = make_big_text(time_str)
    big_time_lines = big_time.split('\n')
    big_time_width = max(len(line)
                         for line in big_time_lines) if big_time_lines else 0

    # Calculate center padding
    time_padding = max(0, (screen_width - big_time_width) // 2)
    date_padding = max(0, (screen_width - len(date_str)) // 2)

    # Calculate vertical centering (~20 lines for 320px height)
    # Big time takes ~3 lines, date takes ~1 line
    vertical_padding_top = 5

    # Add vertical padding to center on screen
    print('\n' * vertical_padding_top)

    # Time - 3x bigger and centered (main focus)
    for line in big_time_lines:
        print(' ' * time_padding + line)
    print('\n' * 4)

    # Date - below the time, centered
    print(' ' * date_padding + date_str)

    # Footer padding to fill screen
    print('\n' * 4)


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
