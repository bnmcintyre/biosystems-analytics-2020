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
    seq = args.seq.upper()

    codons = {}

    for line in args.codons:
        codon, aa = line.rstrip().split()
        codons.update({codon:aa})

    my_codons = []

    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
        my_codons.append(codons.get(codon, '-'))

    out = open(args.out, 'wt')
    out.write(''.join(my_codons) + '\n')
    out.close()

    print(f'Output written to "{args.out}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
