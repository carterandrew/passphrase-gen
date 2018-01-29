# Defines a number of test cases for the passphrase and random string generation

import passLib
from nose.tools import assert_equals
import random

#wordsDefault = ['a','bb','ccc','dddd','eeeee','ffffff','ggggggg','hhhhhhhh','iiiiiiiii','jjjjjjjjjj','kkkkkkkkkkk']
testDict = 'tests/testDict.txt'
randStr = ''


#####################################
# Dictionary validity
#####################################
def test_normal_dict():
  words = passLib.load_word_list('/usr/share/dict/words')
  assert len(words) > 0

def test_none_dict():
  words = passLib.load_word_list(None)
  assert words is None

def test_missing_dict():
  words = passLib.load_word_list('')
  assert words is None


#####################################
# Getting a word from the dictionary 
#####################################
def test_word_from_empty_dict():
  words = []  
  word = passLib.get_word(words)
  assert word is None

def test_word_from_single_word_dict():
  words = ['word']  
  assert_equals(passLib.get_word(words), 'word')

def test_word_from_normal_dict():
  words = passLib.load_word_list('/usr/share/dict/words')
  word = passLib.get_word(words)
  assert word in words

def check_len(exp, actual):
  assert exp == actual

def test_word_min_max_length():
  for i in range(1,12):
    words = passLib.load_word_list(testDict, i, i)
    word = passLib.get_word(words)
    yield check_len, i, len(word)

def test_word_min_out_of_bounds():
  assert_equals(passLib.load_word_list(testDict, minWordLen=-1), None)

def test_word_max_out_of_bounds():
  assert_equals(passLib.load_word_list(testDict, None, -1), None)

def test_word_min_gt_max_length():
  assert_equals(passLib.load_word_list(testDict, 2, 1), None)

def test_word_min_and_max_equal():
  words = passLib.load_word_list(testDict, 2, 2)
  assert_equals(passLib.get_word(words), 'bb')

def test_word_max_len_zero():
  assert_equals(passLib.load_word_list(testDict, 0, 0), [])


####################################
# Getting n words
####################################
def test_n_words_zero():
  words = passLib.load_word_list(testDict, None, 0)
  assert_equals(passLib.get_n_words(words, 1), None)

def test_n_words_single():
  words = passLib.load_word_list(testDict)
  eVal  = random.SystemRandom().choice(words)
  words = passLib.load_word_list(testDict, len(eVal), len(eVal))
  assert_equals(passLib.get_n_words(words, 1), [eVal])

def test_n_words_negative():
  words = passLib.load_word_list(testDict, -1)
  assert_equals(passLib.get_n_words(words, -1), None)

def test_n_words_more_than_wordlist():
  words = passLib.load_word_list(testDict)
  assert_equals(passLib.get_n_words(words, len(words)+1), None)


####################################
# Building a passphrase
####################################
def test_passp_no_words():
  words = passLib.load_word_list(testDict)
  words = passLib.get_n_words(words, 0)
  assert_equals(passLib.build_word_string(words), None)
  words = []
  assert_equals(passLib.build_word_string(words), None)

def test_passp_one_word():
  wordsDefault = passLib.load_word_list(testDict)
  eVal = random.SystemRandom().choice(wordsDefault)
  wordsDefault = passLib.load_word_list(testDict, len(eVal), len(eVal))
  words = passLib.get_n_words(wordsDefault, 1)
  assert_equals(passLib.build_word_string(words), eVal)

def test_passp_two_words_vary_seps():
  wordsDefault = passLib.load_word_list(testDict)
  eVal1 = random.SystemRandom().choice(wordsDefault)
  eVal2 = random.SystemRandom().choice(wordsDefault)
  while(eVal2 == eVal1):
    eVal2 = random.SystemRandom().choice(wordsDefault)
  words = []
  separators = [' ',',','.','-','_','  ','#','*']
  wordList1 = passLib.load_word_list(testDict, len(eVal1), len(eVal1))
  wordList2 = passLib.load_word_list(testDict, len(eVal2), len(eVal2))
  words.append(passLib.get_word(wordList1))
  words.append(passLib.get_word(wordList2))
  for i in range(0,len(separators)):  
    yield passLib.build_word_string, words, eVal1+separators[i]+eVal2

