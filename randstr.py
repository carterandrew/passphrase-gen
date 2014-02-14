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

def_length = 10
digit_chars 	= ['0','1','2','3','4','5','6','7','8','9']
alpha_lower 	= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_upper 	= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','`','~',' ','<',',','>','.','?','/','\\','|',':',';']
default_chars	= digit_chars + alpha_lower + alpha_upper + special_chars
chars = []
rand_s = ''

# Setup the program arguments
parser = argparse.ArgumentParser(description="Simple command-line note taking app")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("-d", "--digit", action="store_true", help="Digits")
parser.add_argument("-a", "--alpha", action="store_true", help="Alphas")
parser.add_argument("-x", "--hexa", action="store_true", help="Hexadecimal")
parser.add_argument("-s", "--special", action="store_true", help="Special")
group.add_argument("-l", "--lower", action="store_true", help="Lowercase")
group.add_argument("-u", "--upper", action="store_true", help="Uppercase")
parser.add_argument("length", type=int, nargs='?', default=def_length, help="Number of characters")
args = parser.parse_args()

pw_length = args.length

# use the default characters if nothing else specified
# hexadecimal doesn't make sense with other options
if (not args.digit and not args.alpha and not args.hexa and not args.special):
  chars = default_chars
else:
  if (args.hexa):
    chars = digit_chars + alpha_lower[:6]
    if (args.upper):
      chars = digit_chars + alpha_upper[:6]
  else:
    if (args.digit):
      chars += digit_chars
    if (args.alpha):
      if (args.upper):
        chars += alpha_upper
      elif (args.lower):
        chars += alpha_lower
      else:
        chars += alpha_upper + alpha_lower
    if (args.special):
      chars += special_chars
  
for i in range(0,pw_length):
  ch = random.SystemRandom().choice(chars)
  rand_s += str(ch)

print(rand_s)
