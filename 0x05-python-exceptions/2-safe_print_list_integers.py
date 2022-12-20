#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cnt = 0
        ptd = 0
        for item in my_list:
            cnt += 1
        if x > cnt:
            raise IndexError
        for item in range(0, x):
            try:
                print("{:d}".format(my_list[item]), end='')
                ptd += 1
            except (ValueError, TypeError):
                continue
        print()
        return (ptd)
    except (TypeError, IndexError):
        print("IndexError: list index out of range")
