#!/usr/bin/python3
"""This module provides a function to print a full name."""


def say_my_name(first_name, last_name=""):
    """Prints: My name is <first_name> <last_name>

    Args:
        first_name (str): First name.
        last_name (str): Last name (optional).

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
