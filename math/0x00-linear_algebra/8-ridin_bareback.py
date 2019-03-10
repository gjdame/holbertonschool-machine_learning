#!/usr/bin/env python3
''' multiply some matricies'''


def mat_mul(mat1, mat2):
    ''' multiply matricies without numpy '''
    res = []
    # if length of rows of mat1 do not equal length of colums of mat2
    if len(mat1[0]) != len(mat2):
        return None
    # over length of colums of mat1
    for i in range(len(mat1)):
        # build rows
        row = []
        # over length of rows of mat2
        for j in range(len(mat2[0])):
            s = 0
            # over length of rows of mat1
            for k in range(len(mat1[0])):
                s += mat1[i][k] * mat2[k][j]
            row.append(s)
        res.append(row)
    return(res)
