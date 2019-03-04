#!/usr/bin/env python3

"""add arrays"""


def add_arrays(arr1, arr2):
    """ add arrays"""
    if len(arr1) != len(arr2):
        return

    res = []
    for i in range(len(arr1)):
        print(i)
        res.append(arr1[i] + arr2[i])

    return(res)
