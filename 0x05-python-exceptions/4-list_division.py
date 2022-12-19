#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        if list_length > max(my_list_1, my_list_2):
            raise IndexError

        idx = 0
        new_list = []
        for item in my_list_1:
            if type(item) != int and type(item) != float:
                raise TypeError
            new_list[idx] = my_list_1[idx] / my_list_2[idx]
        return (new_list)

    except IndexError:
        print("out of range")
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")