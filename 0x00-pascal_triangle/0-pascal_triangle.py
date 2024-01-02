#!/usr/bin/python3
"""
Defines a pascal_triangle function
"""


def pascal_triangle(n):
    """Returns a list of lists that forms Pascal's triangle"""
    pascal_list = []

    if n <= 0:
        return pascal_list

    pascal_list.append([1])
    for i in range(n - 1):
        prev = pascal_list[-1]
        curr = [1]
        for j in range(len(prev) - 1):
            curr.append(prev[j] + prev[j+1])
        curr.append(1)
        pascal_list.append(curr)
    return pascal_list
