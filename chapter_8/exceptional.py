import sys
from math import log
from os import system


DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def convert(s):
    """ Convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",file=sys.stderr)
        raise
    
def string_log(s):
    v = convert(s)
    return log(v)

if __name__ == '__main__':
    system("clear")
    #print(convert("one two three".split()))
    #print(string_log("one two three".split()))
    print(string_log("ouch!".split()))