#!/usr/bin/python

'''
    Generates a string of random words based on several parameters.
    Note that words with apostrophes in them are removed from the list.

    Copyright 2014 Andrew C. Carter
    Released under the terms of the MIT license.
'''

import random
import os
import sys
import argparse
import re
from io import open

def_length = 4
min_word_len = 4
max_word_len = None
word_sep = ' '
words = []
rand_s = ''
wordList = '/usr/share/dict/words'

# Setup the program arguments
parser = argparse.ArgumentParser(description="Basic dictionary word passphrase generator")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("-m", "--minwordlen", help="Minimum word length")
parser.add_argument("-M", "--maxwordlen", help="Maximum word length")
parser.add_argument("-w", "--wordlist", help="Path to wordlist")
parser.add_argument("-s", "--separator", help="Word separator")
group.add_argument("-l", "--lower", action="store_true", help="Lowercase")
group.add_argument("-u", "--upper", action="store_true", help="Uppercase")
group.add_argument("-c", "--capitalize", action="store_true", help="Capitalize")
parser.add_argument("length", type=int, nargs='?', default=def_length, help="Number of words")
args = parser.parse_args()

# Deal with supplied arguments
num_words = args.length
if (args.wordlist is not None):
  wordList = args.wordlist
if (args.minwordlen is not None):
  min_word_len = int(args.minwordlen)
if (args.maxwordlen is not None):
  max_word_len = int(args.maxwordlen)
if (args.separator is not None):
  word_sep = args.separator

# Load the word list
print("Using word list at: "+wordList)
with open(wordList, "r", encoding='utf-8') as f:
  for word in f:
    word = word.strip()
    wl = len(word)
    if (re.search(r'\'',word) or wl < min_word_len or (max_word_len is not None and wl > max_word_len)):
      continue
    words.append(word)

# Bail if there aren't any words to choose from
print("Total available words: "+str(len(words)))
if (len(words) == 0):
  print("No words were found. Perhaps the supplied parameters were too restrictive?")
  exit(1)

# Build the string of words
for i in range(0,num_words):
  word = random.SystemRandom().choice(words)
  if (args.upper):
    word = word.upper()
  elif (args.capitalize):
    word = word.capitalize()
  else:
    word = word.lower()

  if (i > 0):
    rand_s += word_sep
  rand_s += word

print("'"+rand_s+"'")
