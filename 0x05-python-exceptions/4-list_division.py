#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l1 = my_list_1
    l2 = my_list_2
    try:
        for j in l2:
            if j == 0:
                print("division by 0")

        if not (isinstance(l1, (int, float)) and isinstance(l2, (int, float))):
            print("wrong type")

        if list_length > len(l1) or list_length > len(l2):
            raise IndexError

    except IndexError:
        print("out of range")

    finally:
        aux = max(l1, l2)
        new_list = []
        for i in range(len(aux)):
            if isinstance(aux[i], (int, float)) and l2[i]:
                if isinstance(l2[i], (int, float)):
                    new_list.append(aux[i] / l2[i])
                else:
                    new_list.append(0)
            else:
                new_list.append(0)
        return (new_list)
