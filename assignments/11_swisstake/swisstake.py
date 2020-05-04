#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-04-27
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Swiss file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        required=True,
                       # nargs='+',
                        metavar='keyword',
                        type=str)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        nargs='*',
                        type=str)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')


    return parser.parse_args()


#-----------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa))

    skipped = 0
    taken = 0

    for rec in SeqIO.parse(args.file, "swiss"):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                skipped += 1
                continue

        keywords = annots.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if wanted_kw.intersection(keywords):
                taken += 1
                SeqIO.write(rec, args.outfile, 'fasta-2line')
            else:
                skipped += 1
                SeqIO.write(rec, args.outfile, 'fasta')

    print(f'Done, skipped {skipped} and took {taken}. '
          f'See output in "{args.outfile.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
