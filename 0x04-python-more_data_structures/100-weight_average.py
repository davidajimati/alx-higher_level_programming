#!/usr/bin/python3
# Function to calcutate weighted average
def weight_average(my_list=[]):
    # if list is empty return 0
    if not my_list or len(my_list) == 0:
        return (0)

    # declare variable to hold answer and the division of mul cell
    answer = 0
    mul = 0
    den = 0

    # loop through the list and effect the calculations
    for i in my_list:
        mul += i[0] * i[1]
        den += i[1]
    answer = mul / den
    return (answer)
