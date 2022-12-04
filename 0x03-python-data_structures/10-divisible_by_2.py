#!/usr/bin/python3
# Funtion to retun a list of (TRUE or FALSE) based on if
# a number is divisible by 2
def divisible_by_2(my_list=[]):
    lst = []
    for i in my_list:
        if i % 2 == 0:
            lst.append(True)
        else:
            lst.append(False)
    return lst
