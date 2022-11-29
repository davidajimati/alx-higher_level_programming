#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char == 101 or char == 113:
        continue
    print("{:c}" .format(char), end='')