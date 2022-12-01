#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv

    sum = 0
    if len(argv) == 1:
        print(sum)
    else:
        for i in range(len(argv)):
            if i == 0:
                continue
            sum = sum + int(argv[i])
        print(sum)
