#!/usr/bin/env python3

'''
    Generates a string of random words based on several parameters.
    Note that words with apostrophes in them are removed from the list.

    Copyright 2022 Andrew C. Carter
    Released under the terms of the MIT license.
'''

import random
import os
import sys
import argparse
import re
import passLib

DEF_NUM_WORDS = 4
DEF_WORDLIST_PATH = '/usr/share/dict/words'
DEF_MIN_WORD_LEN = 4
DEF_NUM_PHRASES = 1
DEF_WORD_SEPARATOR = ' '

words = []
randStr = ''

parser = argparse.ArgumentParser(description="Basic dictionary word passphrase generator")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("-m", "--minwordlen", type=int, default=DEF_MIN_WORD_LEN, help="Minimum word length")
parser.add_argument("-M", "--maxwordlen", type=int, help="Maximum word length")
parser.add_argument("-n", "--numphrases", type=int, default=DEF_NUM_PHRASES, help="Number of phrases to display")
parser.add_argument("-w", "--wordlist", default=DEF_WORDLIST_PATH, help="Path to wordlist")
parser.add_argument("-s", "--separator", default=DEF_WORD_SEPARATOR, help="Word separator")
parser.add_argument("-q", "--quote", type=bool, default=False, help="Quote output")
group.add_argument("-l", "--lower", action="store_true", help="Lowercase")
group.add_argument("-u", "--upper", action="store_true", help="Uppercase")
group.add_argument("-c", "--capitalize", action="store_true", help="Capitalize")
parser.add_argument("length", type=int, nargs='?', default=DEF_NUM_WORDS, help="Number of words")
args = parser.parse_args()

numWords = args.length
wordListPath = args.wordlist
minWordLen = int(args.minwordlen)
numPhrases = int(args.numphrases)
maxWordLen = int(args.maxwordlen) if args.maxwordlen else None
wordSep = args.separator
quote = args.quote

words = passLib.load_word_list(wordListPath, minWordLen, maxWordLen)
if len(words) < numWords:
    print("Less than %d words present in dictionary. Perhaps the supplied parameters were too restrictive?" % numWords)
    exit(1)

randStrs = []
for _ in range(numPhrases):
  wordsSelected = passLib.get_n_words(words, numWords)

  if not wordsSelected or len(wordsSelected) < numWords:
    print("Less than %d words were found. Perhaps the supplied parameters were too restrictive?" % numWords)
    exit(1)

  randStrs.append(passLib.build_word_string(wordsSelected, wordSep, args.upper, args.capitalize))

passLib.display_phrases(randStrs, quote=quote)
