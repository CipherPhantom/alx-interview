#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the
fewest number of operations needed to result in exactly n H characters
in the file.
"""


def minOperations(n):
    """Calculates and Returns the fewest number of operations"""
    operations = 0
    curr = 1
    copy = 0

    if type(n) != int:
        return operations

    while curr < n:
        if n % curr == 0:
            copy = curr
            curr += copy
            operations += 2
        else:
            curr += copy
            operations += 1
        # print(f"{curr} {'H' * curr}")
    return operations
