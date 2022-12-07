#!/usr/bin/python3
def uniq_add(my_list=[]):
    nset = set(my_list)
    ans = 0
    for i in nset:
        ans += i
    return (ans)
