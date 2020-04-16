#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-04-14
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file by CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        required=True)


    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True)


    parser.add_argument('-o',
                        '--outfile',
                        help='output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    clustered_ids = set() # a set is a unique list (does not repeat elements)

    for line in args.cdhit:
        if line.startswith('>'): # never throws an exception
            continue

        match = re.search(r'>(\d+)', line) # \d means any digit, + means one or more
        if match:
            clustered_ids.add(match.group(1))


    num_written = 0
    num_total = 0
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        num_total += 1
        protein_id = re.sub(r'\|.*', '', rec.id)

        if protein_id not in clustered_ids:
            SeqIO.write(rec, args.outfile, 'fasta')
            num_written += 1

    print(f'Wrote {num_written:,} of {num_total:,} unclustered proteins to "{args.outfile.name}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
