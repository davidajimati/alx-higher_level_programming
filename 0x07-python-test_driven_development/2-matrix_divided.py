#!/usr/bin/python3
'''
Function to divide all the elements in a matrix
'''


def matrix_divided(matrix, div):
    '''
    Function accepts two values
    matrix - the list of lists
    div - denominator
    '''
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_mat = []
    new = 0
    prev = 0
    for i in matrix:
        prev = new
        if new != prev:
            raise TypeError("Each row of the matrix must have the same size")
        new = len(i)
        app = list(map(lambda x: round(x / div, 2), i))
        new_mat.append(app)
        new = len(i)

        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    return new_mat


if __name__ ==  "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
