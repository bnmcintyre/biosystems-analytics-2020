#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-04-14
Purpose: Find PCR Primers and parameters
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find PCR primers and Parameters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        #type=argparse.FileType('r'),
                        help='Target DNA sequence')

    parser.add_argument('-l',
                        '--length',
                        help='length of primers',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--samples',
                        help='number of samples to analyze',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-v',
                        '--volume',
                        help='reaction volume',
                        metavar='int',
                        type=int,
                        default=20)

    parser.add_argument('-a',
                        '--amount',
                        help='amount of DNA for each reaction',
                        metavar='int',
                        type=int,
                        default=5)

    parser.add_argument('-o',
                        '--outfile',
                        help='output file name',
                        metavar='FILE',
                        default='out_pcr')


    args = parser.parse_args()

    if args.length <= 0:
        parser.error(f'Primer length "{args.length}" must be greater than 0.')

    if args.samples <= 0:
        parser.error(f'Sample number "{args.samples}" must be greater than 0.')

    if args.volume <= 0:
        parser.error(f'Reaction volume "{args.volume}" must be greater than 0.')

    if args.amount <= 0:
        parser.error(f'Amount of DNA "{args.amount}" must be greater than 0.')

    if len(args.seq) < args.length:
        parser.error(f'Sequence length of "{len(args.seq)}" must be longer than primer '
                     f'length of "{args.length}"')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq.upper()
    length = args.length
    out = args.outfile
    amount = args.amount
    vol = args.volume
    num = args.samples

    nucs = dict(A='T', T='A', G='C', C='G')

    rev = []
    for i in range(-length, 0):
        if seq[i] in nucs:
            rev.append(nucs.get(seq[i]))

    fwd = []
    for i in range(0, length):
        fwd.append(seq[i])

    fwd = ''.join(fwd)
    rev = ''.join(rev) # figure out how to flip this to print 5-3?

    fA, fT, fG, fC = 0, 0, 0, 0
    for i in range(len(fwd)):
        if fwd[i] == 'A':
            fA += 1
        if fwd[i] == 'T':
            fT += 1
        if fwd[i] == 'G':
            fG += 1
        if fwd[i] == 'C':
            fC += 1

    rA, rT, rG, rC = 0, 0, 0, 0
    for i in range(len(rev)):
        if rev[i] == 'A':
            rA += 1
        if rev[i] == 'T':
            rT += 1
        if rev[i] == 'G':
            rG += 1
        if rev[i] == 'C':
            rC += 1

    TmF = 2 * (fA + fT) + 4 * (fG + fC)
    TmR = 2 * (rA + rT) + 4 * (rG + rC)

    polymerase = (vol/2) * num
    primers = (vol/50) * .4 * num
    bsa = (vol/20) * num
    water = ((vol - amount) * num) - ((polymerase + (2 * primers) + bsa))


    outname = open(args.outfile, 'wt')
    outname.write(
        f'Forward Primer in 5-3: "{fwd}"' + '\n'
        f'Reverse Primer in 3-5: "{rev}"' + '\n'
        f'Tm Forward = "{TmF}C"' + '\n'
        f'Tm Reverse = "{TmR}C"' + '\n'
        f'Polymerase: {polymerase} uL' + '\n'
        f'Forward Primer: {primers} uL' + '\n'
        f'Reverse Primer: {primers} uL' + '\n'
        f'BSA: {bsa} uL' + '\n'
        f'Water: {water} uL' + '\n'
    )
    outname.close()

    print(f'Done, check user directory for outfile {out}.')



# --------------------------------------------------
if __name__ == '__main__':
    main()
