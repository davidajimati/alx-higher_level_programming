#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    from calculator_1 import *

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = argv[3]

        match operator:
            case '+':
                print("{:d}" .format(int(argv[2]) + int(argv[4])))
            case '-':
                print("{:d}" .format(int(argv[2]) - int(argv[4])))
            case '/':
                print("{:d}" .format(int(argv[2]) / int(argv[4])))
            case '*':
                print("{:d}" .format(int(argv[2]) * int(argv[4])))
    sys.exit(0)
