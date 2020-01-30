#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-01-28
Purpose: Find a given vowel in a given word
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='str',
                        help='A Vowel',
                        choices=['A','a','E','e','I','i','O','o','U','u'])

    parser.add_argument('text',
                        help='Some Text',
                        metavar='str')

    return parser.parse_args()

def search_vowel(args):
    text = args.text
    vowel = args.vowel
    wordwrite = False
    thisindex = 0
    for i in range(len(text)):
        if text[i] == vowel:
            wordwrite = True
            thisindex = i
    if wordwrite:
        return print(f'Found "{vowel}" in "{text}" at index {thisindex}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    search_vowel(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
