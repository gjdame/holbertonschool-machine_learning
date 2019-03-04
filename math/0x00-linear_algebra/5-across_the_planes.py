#!/usr/bin/env python3


def add_matrices2D(mat1, mat2):
    """add matricies"""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return
    res = []
    for x in range(len(mat1)):
        r = []
        for i in range(len(mat1[0])):
            r.append(mat1[x][i] + mat2[x][i])
        res.append(r)
    return(res)


def matrix_shape(matrix):
    """Python function to find dimension of matrix"""
    res = []
    shape(res, matrix)
    return(res)


def shape(res, matrix):
    """Python function to find dimension of matrix"""
    if type(matrix) is int:
        return
    for arr in matrix:
        res.append((len(matrix)))
        return(shape(res, arr))
