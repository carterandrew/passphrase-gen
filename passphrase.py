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
import passLib

DEFAULT_NUM_WORDS = 4
DEFAULT_WORDLIST_PATH = '/usr/share/dict/words'
minWordLen = 4
maxWordLen = None
wordSep = ' '
words = []
randStr = ''
wordListPath = DEFAULT_WORDLIST_PATH
numPhrases = 1

# Setup the program arguments
parser = argparse.ArgumentParser(description="Basic dictionary word passphrase generator")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("-m", "--minwordlen", type=int, help="Minimum word length")
parser.add_argument("-M", "--maxwordlen", type=int, help="Maximum word length")
parser.add_argument("-n", "--numphrases", type=int, help="Number of phrases to display")
parser.add_argument("-w", "--wordlist", help="Path to wordlist")
parser.add_argument("-s", "--separator", help="Word separator")
group.add_argument("-l", "--lower", action="store_true", help="Lowercase")
group.add_argument("-u", "--upper", action="store_true", help="Uppercase")
group.add_argument("-c", "--capitalize", action="store_true", help="Capitalize")
parser.add_argument("length", type=int, nargs='?', default=DEFAULT_NUM_WORDS, help="Number of words")
args = parser.parse_args()

# Handle supplied arguments
numWords = args.length
if (args.wordlist is not None):
  wordListPath = args.wordlist
if (args.minwordlen is not None):
  minWordLen = int(args.minwordlen)
if (args.numphrases is not None):
  numPhrases = int(args.numphrases)
if (args.maxwordlen is not None):
  maxWordLen = int(args.maxwordlen)
if (args.separator is not None):
  wordSep = args.separator

words = passLib.load_word_list(wordListPath, minWordLen, maxWordLen)
if (len(words) < numWords):
    print("Less than %d words present in dictionary. Perhaps the supplied parameters were too restrictive?" % numWords)
    exit(1)
randStrs = []
for i in range(0, numPhrases):
  wordsSelected = passLib.get_n_words(words, numWords)

  # Bail if there aren't any words to choose from based on word length requirements
  if (wordsSelected is None or len(wordsSelected) < numWords):
    print("Less than %d words were found. Perhaps the supplied parameters were too restrictive?" % numWords)
    exit(1)

  # Build the string of words
  randStrs.append(passLib.build_word_string(wordsSelected, wordSep, args.upper, args.capitalize))

passLib.display_phrases(randStrs)
