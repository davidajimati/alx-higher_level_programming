#!/usr/bin/python3
# FUNTION TO CONVERT ROMAN NUMRALS TO INTEGER (ARABIC)
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)

    for i in roman_string:
        if i.islower() or type(i) != str:
            return (0)

    roman_to_int_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    prev = 0

    for ch in roman_string[::-1]:
        curr = roman_to_int_map[ch]

        if curr >= prev:
            result += curr
        else:
            result -= curr

        prev = curr

    return result
