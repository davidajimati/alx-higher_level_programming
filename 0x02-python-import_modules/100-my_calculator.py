#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    from calculator_1 import *

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        match operator:
            case '+':
                print("{:d}" .format(add(a, b)))
            case '-':
                print("{:d}" .format(sub(a, b)))
            case '/':
                print("{:d}" .format(div(a, b)))
            case '*':
                print("{:d}" .format(mul(a, b)))
        sys.exit(0)
