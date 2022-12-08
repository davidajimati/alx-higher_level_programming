def roman_to_int(roman_string):
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

        # If the current character has a value greater than or equal to the previous character, we add it to the result
        if curr >= prev:
            result += curr
        else:
            # If the current character has a value less than the previous character, we subtract it from the result
            result -= curr

        prev = curr

    return result

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))