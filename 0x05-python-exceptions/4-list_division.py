#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    # tot = max(my_list_1, my_list_2)
    count = 0
    answer = 0

    for i in range(len(my_list_1)):
        try:
            answer = my_list_1[i] / my_list_2[i]
        except TypeError:
            answer = 0
            print("wrong type")
        except ZeroDivisionError:
            answer = 0
            print("division by 0")
        except IndexError:
            answer = 0
            print("out of range")
        finally:
            new.append(answer)

    return (new)
