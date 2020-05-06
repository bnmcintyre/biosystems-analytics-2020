#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-04-14
Purpose: Find PCR Primers and parameters
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find PCR primers and Parameters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='Target DNA Sequence', help='Target DNA sequence')

    parser.add_argument('-l',
                        '--length',
                        help='length of primers',
                        metavar='Primer length',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--samples',
                        help='number of samples to analyze',
                        metavar='Number of samples',
                        type=int,
                        default=10)

    parser.add_argument('-v',
                        '--volume',
                        help='reaction volume',
                        metavar='reaction volume',
                        type=int,
                        default=20)

    parser.add_argument('-a',
                        '--amount',
                        help='amount of DNA for each reaction',
                        metavar='amount of DNA per reaction',
                        type=int,
                        default=5)

    parser.add_argument('-p',
                        '--primerfinal',
                        help='final concentraton of primer in uM',
                        metavar='final primer concentration',
                        type=float,
                        default=0.4)

    parser.add_argument('-i',
                        '--primerinitial',
                        help='initial concentration of primer uM',
                        metavar='initial primer concentration',
                        type=float,
                        default=50)

    parser.add_argument('-g',
                        '--polyinitial',
                        help='initial concentration of polymerase',
                        metavar='initial polymerase concentration',
                        type=int,
                        default=2)

    parser.add_argument('-b',
                        '--bsainitial',
                        help='initial concentration of BSA',
                        metavar='initial BSA concentration',
                        type=int,
                        default=20)


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

    if args.polyinitial <= 0:
        parser.error(f'Initial concentration of Polymerase '
                     f'"{args.polyinitial}" must be greater than 0.')

    if args.primerfinal <= 0:
        parser.error(f'Final concentration of primer '
                     f'"{args.primerfinal}" must be greater than 0.')

    if args.primerinitial <= 0:
        parser.error(f'Initial concentration of primer '
                     f'"{args.primerinitial}" must be greater than 0.')

    if args.bsainitial <= 0:
        parser.error(f'Initial concentration of BSA '
                     f'"{args.bsainitial}" must be greater than 0.')

    if len(args.seq) < args.length:
        parser.error(f'Sequence length of "{len(args.seq)}" must be longer '
                     f'than primer length of "{args.length}"')


    return args


# -------------------------------------------------
def base_count(DNA):
    """Counts number of Nucleotides"""

    return DNA.count('A'), DNA.count('T'), DNA.count('G'), DNA.count('C')


# --------------------------------------------------
def test_base_count():
    """test base count"""

    assert (0, 0, 0, 0) == base_count('')
    assert (1, 0, 0, 0) == base_count('A')
    assert (0, 1, 0, 0) == base_count('T')
    assert (0, 0, 1, 0) == base_count('G')
    assert (0, 0, 0, 1) == base_count('C')
    assert (2, 1, 3, 2) == base_count('AACCGGGT')
    assert (2, 1, 3, 2) == base_count('ACTGACGG')



# --------------------------------------------------
def melt_temp_calc(calc):
    """calculate melting temperature"""

    return (2 * (calc[0] + calc[1])) + (4 * (calc[2] + calc[3]))

# --------------------------------------------------
def test_melt_temp_calc():
    """test melt temp calculation"""
    calc = (0, 0, 0, 0)
    assert 0 == melt_temp_calc(calc)
    calc = (2, 6, 1, 1)
    assert 24 == melt_temp_calc(calc)
    calc = (2, 5, 2, 1)
    assert 26 == melt_temp_calc(calc)

# --------------------------------------------------
def calc_polymerase(volume, polyinitial, samples):
    """polymerase calculation"""

    polymerase = (volume / polyinitial) * samples
    return polymerase

# --------------------------------------------------
def test_calc_polymerase():
    """test"""

    assert calc_polymerase(1, 1, 1) == 1
    assert calc_polymerase(0, 1, 0) == 0
    assert calc_polymerase(20, 2, 10) == 100

# --------------------------------------------------
def calc_primers(volume, primerinitial, primerfinal, samples):
     """primer calculation"""

     primers = round((volume / primerinitial) * primerfinal * samples, 1)
     return primers


# --------------------------------------------------
def test_calc_primers():
     """test primer calculation"""

     assert calc_primers(1, 1, 1, 1) == 1
     assert calc_primers(0, 1, 0, 0) == 0
     assert calc_primers(20, 50, 0.4, 10) == 1.6

# --------------------------------------------------
def calc_bsa(volume, bsainitial, samples):
     """calculate BSA"""

     bsa = (volume / bsainitial) * samples
     return bsa


# --------------------------------------------------
def test_calc_bsa():
     """test BSA calculation"""

     assert calc_bsa(0, 1, 0) == 0
     assert calc_bsa(1, 1, 1) == 1
     assert calc_bsa(20, 20, 10) == 10

# --------------------------------------------------
def calc_water(volume, amount, samples, polymerase, primers, bsa):
     """water calculation"""

     water = ((volume - amount) * samples) - ((polymerase + (2 * primers) + bsa))
     return water

# --------------------------------------------------
def test_calc_water():
     """test water calculation"""

     assert calc_water(0, 0, 0, 0, 0, 0) == 0
     assert calc_water(1, 1, 1, 1, 1, 1) == -4

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq, length = args.seq.upper(), args.length
    volume, polyinitial, samples = args.volume, args.polyinitial, args.samples
    amount, primerinitial = args.amount, args.primerinitial
    bsainitial, primerfinal = args.bsainitial, args.primerfinal


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
    fA, fT, fG, fC = base_count(fwd)
    rA, rT, rG, rC = base_count(rev)
    fwd_calc = [fA, fT, fG, fC]
    rev_calc = [rA, rT, rG, rC]

    # Calculates the melting temperature
    TmF = melt_temp_calc(fwd_calc)
    TmR = melt_temp_calc(rev_calc)

    # Calculates the Master Mix volumes for the PCR reaction
    polymerase = calc_polymerase(volume, polyinitial, samples)
    primers = calc_primers(volume, primerinitial, primerfinal, samples)
    bsa = calc_bsa(volume, bsainitial, samples)
    water = calc_water(volume, amount, samples, polymerase, primers, bsa)

    # Prints the output of the program to STDOUT
    print(f'Forward Primer in 5-3: "{fwd}"' + '\n'
                  f'Reverse Primer in 3-5: "{rev}"' + '\n'
                  f'Tm Forward: "{TmF}C"' + '\n'
                  f'Tm Reverse: "{TmR}C"' + '\n'
                  f'Polymerase: {polymerase} uL' + '\n'
                  f'Forward Primer: {primers} uL' + '\n'
                  f'Reverse Primer: {primers} uL' + '\n'
                  f'BSA: {bsa} uL' + '\n'
                  f'Water: {water} uL')

# --------------------------------------------------
if __name__ == '__main__':
    main()
