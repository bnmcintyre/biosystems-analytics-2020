#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-28
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        help='a readable file')

    parser.add_argument('-m',
                        '--min',
                        help='minimum number of lines',
                        metavar='int',
                        type=int,
                        default=0)

    args = parser.parse_args()

    if args.min < 0:
        parser.error('minimum integer value must be greater than 0')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.file:
        wordchange = 0
        word1, word2 = line.split()
        if len(word1) != len(word2):
            wordchange += abs(len(word1) - len(word2))
        for i in range(len(word1)):
            if word1[i] not in word2[i]:
                wordchange += 1
        if wordchange >= args.min:
            print(f'{wordchange:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
