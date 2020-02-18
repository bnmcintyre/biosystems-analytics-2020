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
                        #nargs= '+',
                        help='What Day of the Week is it?')

    return parser.parse_args()

#---------------------------------------------------
def day_dict(args):
    """gets day of the week"""

    feeling = {'Monday': ' I never go to work',
           'Tuesday': ' I stay at home',
           'Wednesday': ' I never feel inclined',
           'Thursday': ", it's a holiday",
           'Friday': 's I detest',
           'Saturday': "Oh, it's much too late on a",
           'Sunday': ' is the day of rest'}

    day = args.day
    excuse = feeling.get(args.day)

    if day in feeling:
        if day[0] in 'MTW':
            print(f'On {day}s{excuse}')
        elif day[0:2] in 'FrSu':
            print(f'And {day}{excuse}')
        elif day[0:3] in 'Sat':
            print(f'{excuse} {day}')
    else:
        day = (f'"{day}"')
        print(f"Can't find {day}")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    day_dict(args)

# --------------------------------------------------
if __name__ == '__main__':
    main()
