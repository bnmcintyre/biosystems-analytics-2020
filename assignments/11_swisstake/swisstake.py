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
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        nargs='+',
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
    keyword = ''.join(args.keyword)
    skiptaxa = ''.join(args.skiptaxa)

    taxonomy = []
    keyword_list = []
    skip = set(map(str.lower, skiptaxa))
    taxa = set(map(str.lower, taxonomy))

    skip_num = 0
    taken = 0

    for rec in SeqIO.parse(args.file, "swiss"):
       keywords = rec.annotations.get('keywords')
       taxonomy.append(rec.annotations.get('taxonomy'))
       if skip.intersection(taxa):
           skip_num += 1
           continue
       if keyword in keywords:
           taken += 1
           keyword_list.append(keyword)
           SeqIO.write(rec, args.outfile, 'fasta')

    print(f'Done, skipped {skip_num} and took {taken}. '
          f'See output in "{args.outfile}.')





# --------------------------------------------------
if __name__ == '__main__':
    main()
