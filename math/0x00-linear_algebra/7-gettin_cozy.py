#!/usr/bin/env python3
"""add matricies"""

def cat_matrices2D(mat1, mat2, axis=0):
    """add matricies"""
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        res = []
        res.extend(mat1)
        res.extend(mat2)
        return(res)
    if axis == 1 and len(mat1) == len(mat2):
        res = []
        for i in range(len(mat1)):
            r = []
            r.extend(mat1[i])
            r.extend(mat2[i])
            res.extend([r])
        return(res)

