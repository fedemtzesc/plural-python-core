import sys

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


if __name__ == '__main__':
    msg = sys.argv[1]
    brd = sys.argv[2]

