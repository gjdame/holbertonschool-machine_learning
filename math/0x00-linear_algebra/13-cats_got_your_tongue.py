#!/usr/bin/env python3
''' concat matricies '''
import numpy as np


def np_cat(mat1, mat2, axis=0):
    res = np.concatenate((mat1, mat2), axis)
    return (res)
