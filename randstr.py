#!/usr/bin/python

'''
    Generates a string of random characters based on several parameters.

    Copyright 2014 Andrew C. Carter
    Released under the terms of the MIT license.
'''

import random
import os
import sys
import argparse
import passLib

DEFAULT_LENGTH = 10
chars = []
randStr = ''

# Setup the program arguments
parser = argparse.ArgumentParser(description="Simple command-line note taking app")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("-d", "--digit", action="store_true", help="Digits")
parser.add_argument("-a", "--alpha", action="store_true", help="Alphas")
parser.add_argument("-x", "--hexa", action="store_true", help="Hexadecimal")
parser.add_argument("-s", "--special", action="store_true", help="Special")
group.add_argument("-l", "--lower", action="store_true", help="Lowercase")
group.add_argument("-u", "--upper", action="store_true", help="Uppercase")
parser.add_argument("length", type=int, nargs='?', default=DEFAULT_LENGTH, help="Number of characters")
args = parser.parse_args()

pwLength = args.length

chars = passLib.get_allowable_chars(args.lower, args.upper, args.alpha, args.digit, args.special, args.hexa) 
randStr = passLib.get_passphrase(chars, pwLength)
print(randStr)
