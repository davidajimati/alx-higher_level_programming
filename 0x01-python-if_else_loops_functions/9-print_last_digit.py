#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10

    if number < 0:
        last = ((number * -1) % 10)
    print(last)
