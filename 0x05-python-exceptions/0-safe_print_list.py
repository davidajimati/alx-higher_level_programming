#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for i in range(x):
            idx += 1

        new_ls = my_list[:idx]
        j = 0
        for elem in new_ls:
            j += 1
        print(*new_ls[:idx], sep='')
        return (j)

    except IndexError:
        print("error occured")
