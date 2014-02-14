passphrase-gen
==

A simple passphrase generator for the terminal.

## License

Passphrase-gen is released under the terms of the MIT license.

## Requirements
A word list with one word per line is required. By default, /usr/share/dict is used as the word list. You can specify a different location with '-s'.

## Usage
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

