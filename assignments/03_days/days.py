#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-13
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Day of the Week',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('day',
                        metavar='str',
                        nargs='+',
                        help='What Day of the Week is it?')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    feeling = {
        'Monday': ' I never go to work',
        'Tuesday': ' I stay at home',
        'Wednesday': ' I never feel inclined',
        'Thursday': ", it's a holiday",
        'Friday': 's I detest',
        'Saturday': "Oh, it's much too late on a",
        'Sunday': ' is the day of rest'}

    day = args.day

    for i in range(len(day)):
        if day[i] in feeling:
            if (day[i])[0:3] in 'MonTueWedThu':
                day1 = day[i]
                print(f'On {day1}s{feeling.get(day1)}')
            elif (day[i])[0:2] in 'FrSu':
                day1 = day[i]
                print(f'And {day1}{feeling.get(day1)}')
            elif (day[i])[0:3] in 'Sat':
                day1 = day[i]
                print(f'{feeling.get(day1)} {day1}')
        else:
            day1 = (f'"{day[i]}"')
            print(f"Can't find {day1}")

# --------------------------------------------------
if __name__ == '__main__':
    main()
