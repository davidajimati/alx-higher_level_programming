#!/usr/bin/python3
# returns the larget number in a list
def max_integer(my_list=[]):
    ans = my_list[0]

    for i in my_list:
        if i > ans:
            ans = i
    return ans
