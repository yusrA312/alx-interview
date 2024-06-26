#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''
    the Pascal's triangle .
    '''
    Pascal = []
    if type(n) is not int or n <= 0:
        return Pascal
    for i in range(n):
        line = []
        for X in range(i + 1):
            if X == 0 or X == i:
                line.append(1)
            elif i > 0 and X > 0:
                line.append(Pascal[i - 1][X - 1] + Pascal[i - 1][X])
        Pascal.append(line)
    return Pascal
