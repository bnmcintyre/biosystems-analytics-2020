#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-01-28
Purpose: Rock the Casbah
"""
#what to learn from this excersize:

#variables are stuck within the function you define them in UNLESS you pass it to the next function.
#if you are looking to see if an index is within a group of letters or numbers (i.e. vowels), do NOT set
#it equal (==) to that group, use the built in function 'in' (as seen in line 38)

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='what is nearby?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nearby',
                        metavar='str',
                        help='the following arguments are required: str')

    return parser.parse_args()


# ---------------------------------------------------
def adjective(args):
    """big Y E E T S"""

    word = args.nearby

    if word[0].lower() in 'a''e''i''o''u':
        print(f'Ahoy, Captain, an {word} off the larboard bow!')
    else:
        print(f'Ahoy, Captain, a {word} off the larboard bow!')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    adjective(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
