import sys


def sqrt(x):
    '''
        Compute sqare roots using the method
        of Heron of Alexandria.

        Args:
            x:  The number for wich the sqare root
                is to be computed.

        Returns: 
            The sqare root of x

        Raises:
            ValueError: if x is negative.
    '''
    if x < 0:
        raise ValueError(
                "Cannot compute square root of"
                f" negative number {x}")

    guess = x 
    i = 0

    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    print(sqrt(4))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print(f"{e!r}", file=sys.stderr)
    
    print("\n*** Programm execution continues " 
          "normally here ***")

if __name__ == '__main__':
    main()
