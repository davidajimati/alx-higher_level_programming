#!/usr/bin/python3
import sys
import hidden_4

for i in dir(hidden_4):
    if i[:2] != "__":
        print(i)
