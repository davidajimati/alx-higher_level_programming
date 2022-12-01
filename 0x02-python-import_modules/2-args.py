#!/usr/bin/python3
import sys
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{:d} arguments." .format(0))
    elif len(argv) == 2:
        print("1 argument:")
        print("{:d}" .format(1), argv[1])
    else:
        print(len(argv) - 1, "arguments:")
        for i in range(len(argv)):
            if i == 0:
                continue
            print("{:d}:" .format(i), argv[i])
