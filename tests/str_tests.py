import passLib
from nose.tools import assert_equals, ok_
import random
import re
import string

randStr = ''
ALPHA_UPPER = list(string.ascii_uppercase)
ALPHA_LOWER = list(string.ascii_lowercase)
HEX_ALL = list(string.hexdigits)
HEX_LOWER = list(string.hexdigits[:16])
HEX_UPPER = list(string.hexdigits[:10]+string.hexdigits[16:])
DIGITS = list(string.digits)
SPECIALS = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','`','~',' ','<',',','>','.','?','/','\\','|',':',';']

def test_allowable_chars_alpha_only():
  assert_equals(passLib.get_allowable_chars(alpha=True), ALPHA_UPPER + ALPHA_LOWER)
  assert_equals(passLib.get_allowable_chars(lower=True, alpha=True), ALPHA_LOWER)
  assert_equals(passLib.get_allowable_chars(upper=True, alpha=True), ALPHA_UPPER)

def test_allowable_chars_digit_only():
  assert_equals(passLib.get_allowable_chars(digit=True), DIGITS)
  assert_equals(passLib.get_allowable_chars(upper=True, digit=True), DIGITS)
  assert_equals(passLib.get_allowable_chars(lower=True, digit=True), DIGITS)

def test_allowable_chars_special_only():
  assert_equals(passLib.get_allowable_chars(special=True), SPECIALS)
  assert_equals(passLib.get_allowable_chars(upper=True, special=True), SPECIALS)
  assert_equals(passLib.get_allowable_chars(lower=True, special=True), SPECIALS)

def test_allowable_chars_hexadecimal_only():
  assert_equals(passLib.get_allowable_chars(hexa=True), HEX_ALL)
  assert_equals(passLib.get_allowable_chars(lower=True, hexa=True), HEX_LOWER)
  assert_equals(passLib.get_allowable_chars(upper=True, hexa=True), HEX_UPPER)

def test_allowable_chars_alpha_and_digits():
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True), DIGITS + ALPHA_UPPER + ALPHA_LOWER)
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True, lower=True), DIGITS + ALPHA_LOWER)
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True, upper=True), DIGITS + ALPHA_UPPER)

def test_allowable_chars_alpha_and_specials():
  assert_equals(passLib.get_allowable_chars(alpha=True, special=True), ALPHA_UPPER + ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(alpha=True, special=True, lower=True), ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(alpha=True, special=True, upper=True), ALPHA_UPPER + SPECIALS)

def test_allowable_chars_digits_and_specials():
  assert_equals(passLib.get_allowable_chars(digit=True, special=True), DIGITS + SPECIALS)
  assert_equals(passLib.get_allowable_chars(digit=True, special=True, lower=True), DIGITS + SPECIALS)
  assert_equals(passLib.get_allowable_chars(digit=True, special=True, upper=True), DIGITS + SPECIALS)

def test_allowable_chars_alpha_digits_and_specials():
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True, special=True), DIGITS + ALPHA_UPPER + ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True, special=True, lower=True), DIGITS + ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(alpha=True, digit=True, special=True, upper=True), DIGITS + ALPHA_UPPER + SPECIALS)

def test_allowable_chars_default():
  assert_equals(passLib.get_allowable_chars(), DIGITS + ALPHA_UPPER + ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(lower=True), DIGITS + ALPHA_LOWER + SPECIALS)
  assert_equals(passLib.get_allowable_chars(upper=True), DIGITS + ALPHA_UPPER + SPECIALS)

def test_string_length():
  for i in range(0,10):
    randLen = random.SystemRandom().randint(1,1000)
    randStr = passLib.get_passphrase(passLib.get_allowable_chars(), randLen)
    assert_equals(len(randStr), randLen)

def get_distribution(allowables, chars, randStr):
    for c in randStr:
        chars[c] += 1
    return chars

def test_string_distribution():
    allowables = passLib.get_allowable_chars()
    chars = {}
    for c in allowables:
        chars[c] = 0

    n = 100000
    for i in range(0,n):
        randStr = passLib.get_passphrase(allowables, 10)
        chars = get_distribution(allowables, chars, randStr)

    print(chars)
    strLen = len(randStr)

    expChars = float((strLen*n) / len(allowables))
    print("exp: %s" % expChars)
    for c, v in chars.items():
        pctDiff = float((v - expChars) / expChars)
        msg = str("Failed char '%s' exp: %s got: %s pct diff: %f" % (c, expChars, v, pctDiff))
        ok_(abs(pctDiff) < 0.05, msg=msg)

