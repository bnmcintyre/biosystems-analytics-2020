#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-03-19
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

    parser.add_argument('-o',
                        '--outdir',
                        help='Output Directory',
                        default='out')

    parser.add_argument('file',
                        help='A DNA Sequence File',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'))


    args = parser.parse_args()

    if os.path.isdir(args.outdir) == False:
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outdir = args.outdir
    file = args.file

    filecount = 0
    seqcount = 0


    for fh in args.file:
        outfile = os.path.join(outdir, os.path.basename(fh.name))
        out = open(outfile, 'wt')

    for file in file:
        filecount += 1
        for line in file:
            line.split(' ')
            rna = line.replace('T', 'U')
            seqcount += 1
            out.write(''.join(rna))
        out.close()


    if seqcount == 1 and filecount == 1:
        print(f'Done, wrote {seqcount} sequence in {filecount} file to directory "{outdir}".')
    elif seqcount > 1 and filecount == 1:
        print(f'Done, wrote {seqcount} sequences in {filecount} file to directory "{outdir}".')
    elif seqcount > 1 and filecount > 1:
        print(f'Done, wrote {seqcount} sequences in {filecount} files to directory "{outdir}".')






# --------------------------------------------------
if __name__ == '__main__':
    main()
