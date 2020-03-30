#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-03-30
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--seqtype',
                        help='Sequence Type: DNA or RNA',
                        nargs='+',
                        choices=['dna', 'rna'],
                        metavar='str',
                        type=str,
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to generate',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='The minimun length of any sequence',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='The maximum length of any sequence',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='The average percentage of GC content for a sequence',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='An integer value to use for the random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-out',
                        '--outfile',
                        help='Name of output file',
                        default='out.fa')

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args

# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))

# --------------------------------------------------
# def test_create_pool():
#  """ Test create_pool """
#
#      state = random.getstate()
#      random.seed(1)
#      assert create_pool(.5, 10, 'dna') == 'AAACCCGGTT'
#      assert create_pool(.6, 11, 'rna') == 'AACCCCGGGUU'
#      assert create_pool(.7, 12, 'dna') == 'ACCCCCGGGGGT'
#      assert create_pool(.7, 20, 'rna') == 'AAACCCCCCCGGGGGGGUUU'
#      assert create_pool(.4, 15, 'dna') == 'AAAACCCGGGTTTTT'
#      random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out = args.outfile
    seqtype = args.seqtype[0].upper() + args.seqtype[1].upper() + args.seqtype[2].upper()
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    outname = open(args.outfile, 'wt')

    for i in range(1, args.numseqs + 1):
        seqlen = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, seqlen))
        outname.write(f'>{i}' + '\n' + seq)
        #print(f'>{i}' + '\n' + seq)

    outname.close()

    print(f'Done, wrote {args.numseqs} {seqtype} sequences to "{out}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
