'''Retrieve and print words from a URL

    Usage:
        python3 banner.py header_text char
'''

import sys


def banner(message, border='-'):
    '''Returns an elegant header with borders uppon and buttom
        
        Args:
            message: Is the message of the header
            border: Is the character o string to use for the border

        Returns:
            A pretty and elegant header with borders
    '''
    line = border * len(message)
    print("\t",line)
    print("\t",message)
    print("\t",line)


if __name__ == '__main__':
    msg = sys.argv[1]
    brd = sys.argv[2]
    banner(msg, brd)