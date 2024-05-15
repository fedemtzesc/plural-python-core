import sys

def banner(message, border='-'):
    line = border * len(message)
    print("\t", line)
    print("\t", message)
    print("\t", line)


if __name__ == '__main__':
    if len(sys.argv)==3:
        msg = sys.argv[1]
        brd = sys.argv[2]
    elif len(sys.argv)==2:
        msg = sys.argv[1]
        brd = "="
    else:
        msg = "NO INTRODUJO NINGUN ARGUMENTO POR LA LINEA DE COMANDOS"
        brd = "="

    banner(msg, brd)
