#!/usr/bin/python3
"""
function that square 
some list of number
in a list
"""
def square_matrix_simple(matrix=[]):
    list_num = []
    for k in matrix:
        result = list(map(lambda x:x**2,k))
        list_num.append(result)

    return list_num
