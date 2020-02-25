#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-20
Purpose: Practice with Files
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Practice with Files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        nargs='?',
                        help='A readable file')


    parser.add_argument('-n',
                        '--num',
                        help='How many lines do you want to see?',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    for _ in range(0,args.num):
        print(args.file.readline(), end='')

# --------------------------------------------------
if __name__ == '__main__':
    main()
