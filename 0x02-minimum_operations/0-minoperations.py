#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the
fewest number of operations needed to result in exactly n H characters
in the file.
"""


def copyAll(string):
    """Returns input string"""
    return string


def paste(string_1, string_2):
    """Concatenates two string"""
    return string_1 + string_2


def minOperations(n):
    """Calculates and Returns the fewest number of operations"""
    operations = 0
    txt_file = "H"
    copy = ""

    if type(n) != int:
        return operations

    while len(txt_file) < n:
        if n % len(txt_file) == 0:
            copy = copyAll(txt_file)
            txt_file = paste(txt_file, copy)
            operations += 2
        else:
            txt_file = paste(txt_file, copy)
            operations += 1
    return operations
