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

    parser.add_argument('seq', metavar='str', help='Target DNA sequence')

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
        parser.error(
            f'Reaction volume "{args.volume}" must be greater than 0.')

    if args.amount <= 0:
        parser.error(f'Amount of DNA "{args.amount}" must be greater than 0.')

    if len(args.seq) < args.length:
        parser.error(
            f'Sequence length of "{len(args.seq)}" must be longer than primer '
            f'length of "{args.length}"')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq.upper()
    length = args.length
    out = args.outfile

    # Creates the Forward and Reverse Primer using string indexing
    nucs = dict(A='T', T='A', G='C', C='G')

    rev_list = []
    for i in range(-length, 0):
        if seq[i] in nucs:
            rev_list.append(nucs.get(seq[i]))

    fwd_list = []
    for i in range(0, length):
        fwd_list.append(seq[i])

    fwd = ''.join(fwd_list)
    rev = ''.join(rev_list)  # figure out how to flip this to print 5-3?

    # Counts the number of each nucleotide in each primer
    fA, fC, fG, fT = base_count(fwd)
    rA, rC, rG, rT = base_count(rev)

    # fA = fwd.count('A')
    # fT = fwd.count('T')
    # fG = fwd.count('G')
    # fC = fwd.count('C')

    # rA = rev.count('A')
    # rT = rev.count('T')
    # rG = rev.count('G')
    # rC = rev.count('C')

    # Calculates the melting temperature
    TmF = 2 * (fA + fT) + 4 * (fG + fC)
    TmR = 2 * (rA + rT) + 4 * (rG + rC)

    # Calculates the Master Mix volumes for the PCR reaction
    # I got these numbers from my labs MM calc - MAY NOT BE ACCURATE
    # This calculator makes a lot of assumptions about your reactions
    polymerase = (args.volume / 2) * args.samples
    primers = round((args.volume / 50) * .4 * args.samples, 1)
    bsa = (args.volume / 20) * args.samples
    water = ((args.volume - args.amount) * args.samples) - (
        (polymerase + (2 * primers) + bsa))

    # Outputs this information to an output file
    outname = open(args.outfile, 'wt')
    outname.write(f'Forward Primer in 5-3: "{fwd}"' + '\n'
                  f'Reverse Primer in 3-5: "{rev}"' + '\n'
                  f'Tm Forward = "{TmF}C"' + '\n'
                  f'Tm Reverse = "{TmR}C"' + '\n'
                  f'Polymerase: {polymerase} uL' + '\n'
                  f'Forward Primer: {primers} uL' + '\n'
                  f'Reverse Primer: {primers} uL' + '\n'
                  f'BSA: {bsa} uL' + '\n'
                  f'Water: {water} uL' + '\n')
    outname.close()

    # Done statement
    print(f'Done, check user directory for outfile {out}.')


# --------------------------------------------------
def base_count(seq):
    """ Count the number of A, C, G, T in a given sequence """

    return seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')


# --------------------------------------------------
def test_base_count():
    """ Test """

    assert (0, 0, 0, 0) == base_count('')
    assert (1, 0, 0, 0) == base_count('A')
    assert (0, 1, 0, 0) == base_count('C')
    assert (0, 0, 1, 0) == base_count('G')
    assert (0, 0, 0, 1) == base_count('T')


# --------------------------------------------------
if __name__ == '__main__':
    main()
