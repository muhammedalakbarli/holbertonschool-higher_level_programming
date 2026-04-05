#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
