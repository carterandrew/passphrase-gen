passphrase-gen
==

Simple passphrase and password generators for the terminal.

## License

Passphrase-gen is released under the terms of the MIT license.

## Requirements
These scripts shoul work on linux in python 2.7+ or 3.X.
#### passphrase.py
A word list with one word per line is required. By default, /usr/share/dict is used as the word list. You can specify a different location with '-s'.

#### randstr.py
No specific requirements.

## Usage
#### passphrase.py
    $ ./passphrase.py --help
    usage: ./passphrase.py [-h] [-m MINWORDLEN] [-M MAXWORDLEN] [-w WORDLIST]
                    [-s SEPARATOR] [-l | -u | -c]
                    [length]

    Basic dictionary word passphrase generator

    positional arguments:
      length                Number of words

    optional arguments:
      -h, --help            show this help message and exit
      -m MINWORDLEN, --minwordlen MINWORDLEN
                            Minimum word length
      -M MAXWORDLEN, --maxwordlen MAXWORDLEN
                            Maximum word length
      -w WORDLIST, --wordlist WORDLIST
                            Path to wordlist
      -s SEPARATOR, --separator SEPARATOR
                            Word separator
      -l, --lower           Lowercase
      -u, --upper           Uppercase
      -c, --capitalize      Capitalize

#### randstr.py
    $ ./randstr.py --help
    usage: randstr.py [-h] [-d] [-a] [-x] [-s] [-l | -u] [length]

    Simple command-line note taking app

    positional arguments:
      length         Number of characters

    optional arguments:
      -h, --help     show this help message and exit
      -d, --digit    Digits
      -a, --alpha    Alphas
      -x, --hexa     Hexadecimal
      -s, --special  Special
      -l, --lower    Lowercase
      -u, --upper    Uppercase

## Examples
###### Generate a six-word passphrase
    $ ./passphrase.py 6
    Using word list at: /usr/share/dict/words
    Total available words: 86382
    'directories encampment cellphone tinkers obtuseness inhibition'

###### Generate a four-word capitalized passphrase with periods as separators
    $ ./passphrase.py -s '.' 4
    Using word list at: /usr/share/dict/words
    Total available words: 86382
    'collar.mandrel.uncleaner.sambaing'

###### Specify a different wordlist
    $ ./passphrase.py -w "/usr/share/dict/cracklib-small"
    Using word list at: /usr/share/dict/cracklib-small
    Total available words: 48221
    'hopkins craters caches anthropology'

###### Generate a 15 digit password
    $ ./randstr.py 15
    =3IAgW7:Tb!ZXG?

###### Generate a password using only letters
    $ ./randstr.py -a
    IdsaBsyDlJ
    
###### Generate a 64 character hexadecimal password
    $ ./randstr.py -x 64
    2774ab418d2d1f9d39ca7310364e12d333b7c579b587c86a18cfdae0baf154d6
  
