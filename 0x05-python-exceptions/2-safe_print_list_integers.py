#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        lent = 0
        for item in my_list:
            lent += 1
        if x >= lent:
            raise IndexError

        new_ls = []
        for item in my_list:
            if type(item) == int:
                new_ls.append(item)

        print("{:d}" .format(*new_ls))
        return (lent)

    except IndexError:
        print("list index out of range")