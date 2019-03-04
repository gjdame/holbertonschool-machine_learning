#!/usr/bin/env python3


def cat_matrices2D(mat1, mat2, axis=0):
    """add matricies"""

    res = []
    if axis == 1:
        res.append(mat1[0] + mat2[0])
        res.append(mat1[1] + mat2[1])
        return(res)
    else:
        res.append(mat1)
        res.append(mat2[0])
        return(res)

