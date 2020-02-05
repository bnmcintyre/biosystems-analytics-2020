#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-02-04
Purpose: Classifies a given input as uppercase, lowercase, title case,
a digit, a space or /, or none of the above
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='user input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='input anything you want')

    return parser.parse_args()

#---------------------------------------------------
def inputchecker(args):

    usrinput = args.input

    stringinput = False
    spaceinput = False
    charinput = False
    digitinput = False


    if usrinput.isdigit() == True:
        digitinput = True
    elif usrinput[0:] in ' ' '\t':
        spaceinput = True
    elif usrinput[0:] in '/.~`][}{";:><+=-_|*&!@#$%^)(':
        charinput = True
    # elif isinstance(usrinput, float) == True:
    #     floatinput = True
    else:
        stringinput = True


    if digitinput:
        print(f'{usrinput} is a digit.')
    elif spaceinput:
        print('input is space.')
    elif charinput:
        print(f'{usrinput} is unclassified.')
    # elif floatinput:
    #     print(f'{usrinput} is unclassified.')
    elif stringinput:
        if usrinput.upper() == usrinput:
            print(f'{usrinput} is uppercase.')
        elif usrinput.lower() == usrinput:
            print(f'{usrinput} is lowercase.')
        elif usrinput.title() == usrinput:
            print(f'{usrinput} is title case.')








    # if usrinput.isdigit() == True:
    #     print(f'{usrinput} is a digit.')
    # else:
    #     strusrinput = True
    #
    # if usrinput == ' ':
    #     spaceinput = True
    #     strusrinput = False
    #     print('input is space.')
    # else:
    #     strusrinput = True
    #
    # if usrinput in '/.~`][}{";:><+=-_|*&!@#$%^)(':
    #     strusrinput = False
    #     print(f'{usrinput} is unclassified.')
    #
    #
    # if strusrinput:
    #     if usrinput.upper() == usrinput:
    #         print(f'{usrinput} is uppercase.')
    #     elif usrinput.lower() == usrinput:
    #         print(f'{usrinput} is lowercase.')
    #     elif usrinput.title() == usrinput:
    #         print(f'{usrinput} is title case.')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputchecker(args)



# --------------------------------------------------
if __name__ == '__main__':
    main()
