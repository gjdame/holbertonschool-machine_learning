#!/usr/bin/env python3
'''add sub mul div numpy'''


def np_elementwise(mat1, mat2):
    ''' add mul div sub with numpy'''
    c = ((mat1 + mat2), (mat1 - mat2), (mat1 * mat2), (mat1 / mat2))
    return (c)
