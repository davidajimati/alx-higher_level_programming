#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for i in range(x):
            idx += 1
        print(*my_list[:idx], sep='')
        print()
        return (idx)
    except:
        print("error occured")
