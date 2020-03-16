#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-03-04
Purpose: Rock the Casbah
"""
from typing import Any

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        nargs='+',
                        help='A Nucleotide Sequence')


    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--out',
                        help='output file name',
                        metavar='str',
                        type=str,
                        default='out.txt')

    return parser.parse_args()



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seq = args.seq
    outname = args.out

    codons = {}

    for line in args.codons:
        codon, aa = line.rstrip().split()
        codons.update({codon:aa})

    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
        if codon in codons: # if I just ask it to print the key pair [print(codons.get(codon)], it doesnt return anything :(
            out = open(outname, 'wt+')
            out.write(codons.get(codon, "codon not found"))
            out.close()

    print(f'output written to "{outname}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
