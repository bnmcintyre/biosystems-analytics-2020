#!/usr/bin/env python3
"""
Author : bnmcintyre
Date   : 2020-01-28
Purpose: Find a given vowel in given text
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments from user"""
    """asks for two inputs - a vowel and some text - returns arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='str',
                        help='A Vowel',
                        choices=['A','a','E','e','I','i','O','o','U','u'])

    parser.add_argument('text',
                        help='Some Text',
                        metavar='str')

    return parser.parse_args()

def search_vowel(args): #passes the arguments from the previous function into this function
    """this function passes the arguments gained in the previous function
    and uses a for loop to compare each letter of the given string to the
    given vowell"""

    text = args.text        #sets the "some text" argument from the parser as the variable 'text' to be used in the for loop
    vowel = args.vowel      #sets the "vowel" argument from the parser as the variable 'vowel' to be used in the for loop
    vowelinword = False     #this is false unless proven true by the for loop - only proven true if the letter at that index is equal to the vowel variable
    thisindex = 0           #establishes 'thisindex' as a variable that changes to the value of the index where the letter equals the vowel variable
    for i in range(len(text)):  #for loop for the length of the text variable
        if text[i] == vowel:    #if the letter at index position i is exactly equal to the given value, then the variable 'vowelinword' becomes true
            vowelinword = True
            thisindex = i   #sets the variable 'thisindex' equal to the index at which the vowel is located to call later
    if vowelinword:   #if this statement becomes true by the vowel being in the text, then it will print the following statement
        return print(f'Found "{vowel}" in "{text}" at index {thisindex}.')
    else:   #if 'vowelinword' is still false by the vowel not being in the text, then it will print the follwing statement
        print(f'"{vowel}" is not found in "{text}".')
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()   #calls get-arg function and sets the variable 'args' equal to the passed arguments in the parser
    search_vowel(args)  #passes the arguments from the parser to the search-vowel function for analysis


# --------------------------------------------------
if __name__ == '__main__':
    main()
