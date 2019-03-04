#!/usr/bin/env python3
"""Python function to find dimension of matrix"""


def matrix_shape(matrix):
    res = []
    shape(res, matrix)
    return(res)


def shape(res, matrix):
    if type(matrix) is int:
        return
    for arr in matrix:
        res.append((len(matrix)))
        return(shape(res, arr))
