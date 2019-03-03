#!/usr/bin/env python3
"""Python function to find dimension of matrix"""

def matrix_shape(matrix):
    """Python function to find dimension of matrix"""
    import numpy as np
    arr = np.array(matrix)
    return (list(arr.shape))
