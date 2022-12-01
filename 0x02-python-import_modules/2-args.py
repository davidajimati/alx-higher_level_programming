#!/usr/bin/python3
import sys
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 Arguments.")
    elif len(argv) == 2:
        print("1 Argument:")
        print("1:", argv[1])
    else:
        print(len(argv) - 1, "Arguments:")
        for i in range(len(argv)):
            if i == 0:
                continue
            print("{:d}:" .format(i), argv[i])
