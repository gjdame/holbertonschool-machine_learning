#!/usr/bin/env python3

"""transpose without numpy"""


def matrix_transpose(matrix):
    """transpose without numpy"""
    res = []
    for i in range(len(matrix[0])):
        r = []
        for j in range(len(matrix[i])):
            r.append(matrix[j][i])
        res.append(r)
    return(res)
