#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-04-07
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Randomly select samples from FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        help='A readable FASTA file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'))

    parser.add_argument('-p',
                        '--pct',
                        help='percentage of reads to take',
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='random seed value',
                        metavar='seed value',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='output directory',
                        default='out')

    args = parser.parse_args()

    if not 0 <= args.pct <= 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    if os.path.isdir(args.outdir) == False:
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    file_num = 0
    num_seq = 0
    for i, fh in enumerate(args.file, start=1):
        file_num += 1
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{i:3}: {basename}')

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                num_seq += 1
        out_fh.close()

    print(f'Wrote {"{:,}".format(num_seq)} sequence{"" if num_seq == 1 else "s"} '
          f'from {file_num} file{"" if file_num == 1 else "s"} '
          f'to directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
