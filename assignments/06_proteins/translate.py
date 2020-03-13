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
                        nargs='*',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--out',
                        help='output file name',
                        metavar='str',
                        type=str,
                        default='out.txt')

    args = parser.parse_args()


    for letter in args.seq:      # I cannot get this to work properly and I have no idea why
        if letter not in 'ATGCU':
           parser.error('codon not found')

    return args

    #return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq
    outname = args.out


    codons = {'CAU': 'H', 'CAC': 'H', 'CGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGU': 'R', 'AGG': 'R', 'AGA': 'R',
              'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UCU': 'S', 'UCC': 'S',
              'UCA': 'S', 'UCG': 'S', 'AGC': 'S', 'AGU': 'S', 'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACU': 'T',
              'AAC': 'N', 'AAU': 'N', 'CAA': 'Q', 'CAG': 'Q', 'UGU': 'C', 'UGC': 'C', 'GGG': 'G', 'GGA': 'G',
              'GGC': 'G', 'GGU': 'G', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'GCG': 'A', 'GCA': 'A',
              'GCC': 'A', 'GCU': 'A', 'GUG': 'V', 'GUA': 'V', 'GUC': 'V', 'GUU': 'V', 'AUA': 'I', 'AUC': 'I',
              'AUU': 'I', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUG': 'M',
              'UUU': 'F', 'UUC': 'F', 'UAU': 'Y', 'UAC': 'Y', 'UGG': 'W', 'UAA': 'STOP', 'UAG': 'STOP',
              'UGA':'STOP'
              }

    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
        if 'T' in seq:
            rnaseq = codon.replace('T','U')
        else:
            rnaseq = seq

        if rnaseq in codons: # I cant get it to output the amino acid sequence into a new file
            out = open(outname, 'w+')     # it was working earlier but something must of happened becuase now
            out.write(codons.get(rnaseq)) # it is not working anymore
            out.close()

    print(f'output written to "{outname}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
