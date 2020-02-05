#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-04
Purpose: count the frequency of the nucleotides in a given piece of DNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='get dna',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dnaseq',
                        metavar='str',
                        help='DNA Sequence')

    return parser.parse_args()
#---------------------------------------------------
def count_nucs(args):
    dnaseq = args.dnaseq

    acount = 0
    tcount = 0
    ccount = 0
    gcount = 0

    for i in range(len(dnaseq)):
        if dnaseq[i].lower() == 'a':
            acount = acount + 1
        elif dnaseq[i].lower() == 't':
            tcount = tcount + 1
        elif dnaseq[i].lower() == 'c':
            ccount = ccount + 1
        elif dnaseq[i].lower() == 'g':
            gcount = gcount + 1

    print(f'{acount} {ccount} {gcount} {tcount}')

    apercent = int((acount/len(dnaseq)) * 100)
    tpercent = int((tcount/len(dnaseq)) * 100)
    cpercent = int((ccount/len(dnaseq)) * 100)
    gpercent = int((gcount/len(dnaseq)) * 100)

    print(f'Percent A: {apercent}, '
          f'Percent T: {tpercent}, '
          f'Percent C: {cpercent}, '
          f'Percet{gcount}')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    count_nucs(args)



# --------------------------------------------------
if __name__ == '__main__':
    main()
