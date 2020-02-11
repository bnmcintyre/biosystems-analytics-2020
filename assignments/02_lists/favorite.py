#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-06
Purpose: aye lmao
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='favorite things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things',
                        metavar='str',
                        nargs='+',
                        help='What are your favorite things?')

    parser.add_argument('-s',
                        '--sep',
                        help='Do you want a non-comma separator?',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()

#---------------------------------------------------
def favorite(args):
    things = args.things

    if len(things) == 1:
        happy = things[0]
        print(f'{happy}\nThis is one of my favorite things.')
    elif len(things) == 2 or 3:
        happy = args.sep.join(things)
        print(f'{happy}\nThese are a few of my favorite things.')

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    favorite(args)

# --------------------------------------------------
if __name__ == '__main__':
    main()
