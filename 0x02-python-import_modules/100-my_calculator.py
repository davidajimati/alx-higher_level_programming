#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    from calculator_1 import add, sub, mul, div
    operators = ['*', '+', '-', '/']

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        operator = argv[2]
        if operator not in operators:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)

        a = int(argv[1])
        b = int(argv[3])

        match operator:
            case '+':
                print("{:d} + {:d} = {:d}" .format(a, b, add(a, b)))
            case '-':
                print("{:d} + {:d} = {:d}" .format(a, b, sub(a, b)))
            case '/':
                print("{:d} + {:d} = {:d}" .format(a, b, div(a, b)))
            case '*':
                print("{:d} + {:d} = {:d}" .format(a, b, mul(a, b)))
        exit(0)
