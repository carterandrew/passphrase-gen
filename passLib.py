import re
import random
import string
from io import open

MAX_WORD_LEN = 100

digit_chars 	= list(string.digits)
alpha_lower 	= list(string.ascii_lowercase)
alpha_upper 	= list(string.ascii_uppercase)
special_chars = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','`','~',' ','<',',','>','.','?','/','\\','|',':',';']
default_chars	= digit_chars + alpha_upper + alpha_lower + special_chars

def get_allowable_chars(lower=False, upper=False, alpha=False, digit=False, special=False, hexa=False):
  # use the default characters if nothing else specified
  # hexadecimal doesn't make sense with other options
  chars = []
  if (not digit and not alpha and not hexa and not special):
    if (not lower and not upper):
      chars = default_chars
    elif (not lower):
      chars = digit_chars + alpha_upper + special_chars
    else:
      chars = digit_chars + alpha_lower + special_chars
  else:
    if (hexa):
      if (upper):
        chars = digit_chars + alpha_upper[:6]
      elif (lower):
        chars = digit_chars + alpha_lower[:6]
      else:
        chars = digit_chars + alpha_lower[:6] + alpha_upper[:6]
    else:
      if (digit):
        chars += digit_chars
      if (alpha):
        if (upper):
          chars += alpha_upper
        elif (lower):
          chars += alpha_lower
        else:
          chars += alpha_upper + alpha_lower
      if (special):
        chars += special_chars
  return chars

def get_passphrase(chars, passLength):
  rand_s = ''
  for i in range(0, passLength):
    ch = random.SystemRandom().choice(chars)
    rand_s += str(ch)
  return rand_s

# Load the word list from the specified path
def load_word_list(wordListPath, minWordLen=None, maxWordLen=None):
  if minWordLen is None:
    minWordLen = 0
  if maxWordLen is None:
    maxWordLen = MAX_WORD_LEN
  if not wordListPath:
    return None
  if minWordLen < 0 or maxWordLen < 0 or maxWordLen < minWordLen:
      return None
  print("Using word list at: "+wordListPath)
  if minWordLen or maxWordLen < MAX_WORD_LEN:
    print("Supplied min/max word length parameters may reduce the sample space.")
  words = []
  try:
    with open(wordListPath, "r", encoding='utf-8') as f:
      for word in f:
        word = word.strip()
        # skip words with apostrophe's
        if (not re.match(r'^[a-zA-Z]+$', word)):
          continue
        wl = len(word)
        if wl < minWordLen:
            continue
        elif maxWordLen and wl > maxWordLen:
            continue
        words.append(word)
  except IOError as e:
    print(e.errno)
    print(e)
    return None
  print("Final dictionary contains %s words" % (len(words)))
  return words

def get_word(words, excludeWords=[]):
  if (words is None or len(words) == 0):
    return None

  numTried = 0
  numWords = len(words)
  while (numTried < numWords):
    word = random.SystemRandom().choice(words)
    if (word in excludeWords):
      numTried += 1
      words.remove(word)
    else:
      return word 
  return None

def display_phrases(phrases):
    for p in phrases:
        print("'%s'" % p)

# returns n words from the supplied wordList
def get_n_words(wordList, n):
  if (n <= 0 or wordList is None or len(wordList) < n): 
    return None
  words = []
  word = get_word(wordList, words)
  while (word is not None and len(words) < n):
    words.append(word)
    word = get_word(wordList, words)
  if (len(words) < n):
    return None
  return words

def build_word_string(wordsSelected, wordSep=' ', upper=False, capitalize=False):
  if (wordsSelected is None or len(wordsSelected) < 1):
    return None
  randStr = ''
  for i in range(0,len(wordsSelected)):
    word = wordsSelected[i]
    if (upper):
      word = word.upper()
    elif (capitalize):
      word = word.capitalize()
    else:
      word = word.lower()

    if (i > 0):
      randStr += wordSep
    randStr += word
  return randStr
