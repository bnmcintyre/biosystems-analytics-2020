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

    if args.num < 1: #ask about how to incorporate this into the actual argparse statement (line 28-33)
        print('Usage: head.py[-h] [-n int] FILE')
        print(f'head.py: error: --num "{args.num}" must be greater than 0')
        sys.exit(1)
    else:
        num = args.num

    lines = args.file.readlines() #ask if manipulating files can ONLY occur where you define them
    for line in range(0,num): #(using type=argparse.filetype('r')) - like how does this line work??
        print(lines[line], end = '') #was having trouble trying to do this when I tried doing it in main instead of get_args

#ERASE ALL COMMENTS AFTER ASKING QUESTIONS TO KEN THEN REPUSH TO GITHUB!!!!!
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
