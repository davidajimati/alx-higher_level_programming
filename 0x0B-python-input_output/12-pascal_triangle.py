#!/usr/bin/python3

'''
Create a function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
'''


def pascal_triangle(n):
    ''' Creates "n" rows of pascal's triangle '''
    ret = [[1]]

    if n <= 0:
        return ret
    if n is None:
        return None

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(ret[i-1][j-1] + ret[i-1][j])
        row.append(1)
        ret.append(row)

    return (ret)
