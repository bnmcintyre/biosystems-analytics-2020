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

    parser.add_argument('-p',
                        '--primerfinal',
                        help='final concentraton of primer in uM',
                        metavar='float',
                        type=float,
                        default=0.4)

    parser.add_argument('-i',
                        '--primerinitial',
                        help='initial concentration of primer uM',
                        metavar='float',
                        type=float,
                        default=50)

    parser.add_argument('-g',
                        '--polyinitial',
                        help='initial concentration of polymerase',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-b',
                        '--bsainitial',
                        help='initial concentration of BSA',
                        metavar='int',
                        type=int,
                        default=20)

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
        parser.error(
            f'Sequence length of "{len(args.seq)}" must be longer than primer '
            f'length of "{args.length}"')

    return args


# -------------------------------------------------
def base_count(seq):
    """Counts number of Nucleotides"""

    return seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')


# --------------------------------------------------
def test_base_count():
    """test"""

    assert (0, 0, 0, 0) == base_count('')
    assert (1, 0, 0, 0) == base_count('A')
    assert (0, 1, 0, 0) == base_count('C')
    assert (0, 0, 1, 0) == base_count('G')
    assert (0, 0, 0, 1) == base_count('T')
    assert (2, 2, 3, 1) == base_count('ACTGACGG')


# --------------------------------------------------
def melt_temp_calc(calc):
    """docstring"""

    return (2 * (calc[0] + calc[1])) + (4 * (calc[2] + calc[3]))


# --------------------------------------------------
def test_melt_temp_calc():
    """test"""

    assert 0 == melt_temp_calc('')
    assert 24 == melt_temp_calc('CTTATTAGTT')
    assert 26 == melt_temp_calc('ATGGTTTCTA')


# --------------------------------------------------


# --------------------------------------------------
def MM_calc(volume, polyinitial, samples, ):
    """calculates MM portions"""

    args = get_args()

    polymerase = (args.volume / args.polyinitial) * args.samples
    primers = round(
        (args.volume / args.primerinitial) * args.primerfinal * args.samples,
        1)
    bsa = (args.volume / args.bsainitial) * args.samples
    water = ((args.volume - args.amount) * args.samples) - (
        (polymerase + (2 * primers) + bsa))

    return polymerase, primers, bsa, water


# --------------------------------------------------
def test_MM_calc():
    """test"""

    assert (100.0, 1.6, 10.0, 36.8) == MM_calc(1, 2, 3, 4)


# --------------------------------------------------
def calc_polymerase(volume, polyinitial, samples):
    """Calculate polymerase"""

    polymerase = (volume / polyinitial) * samples


# --------------------------------------------------
def test_calc_polymerase():
    """Test polymerase"""

    assert calc_polymerase(1, 1, 1) == 1
    assert calc_polymerase(0, 0, 0) == 1


# --------------------------------------------------
# def run():
#     """run and test"""
#
#     out_tmpl = 'Done, check user directory for outfile "{out}".'
#     run_tmpl = '{prg} {file} -o {out_file}'
#     out_file = random_filename()
#
#     if os.path.isfile(out_file):
#         os.remove(out_file)
#     try:
#         cmd = run_tmpl.format(prg=prg,
#                               file=input2,
#                               out_file=out_file)
#
#         rv, out = getstatusoutput(cmd)
#         assert rv == 0
#         assert out.split('\n')[-1] == out_tmpl.format(out=out_file)
#
#     finally:
#         if os.path.isfile(out_file):
#             os.remove(out_file)


# --------------------------------------------------
def test_01():
    """test run 1"""

    # run({
    #     'kw': '"complete proteome"',
    #     'tax': '-s Metazoa FUNGI viridiplantae',
    #     'skipped': 14,
    #     'took': 1
    # })


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
    fwd_calc = [fA, fT, fG, fC]
    rev_calc = [rA, rT, rG, rC]

    # Calculates the melting temperature
    TmF = melt_temp_calc(fwd_calc)
    TmR = melt_temp_calc(rev_calc)

    # Calculates the Master Mix volumes for the PCR reaction
    polymerase, primers, bsa, water = MM_calc()

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
    print(f'Done, check user directory for outfile "{out}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
