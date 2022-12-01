#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 Arguments.")
elif len(sys.argv) == 2:
    print("1 Argument:")
    print("1:", sys.argv[1])
else:
    print(len(sys.argv) - 1, "Arguments:")
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{:d}:" .format(i), sys.argv[i])
