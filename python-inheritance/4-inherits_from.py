#!/usr/bin/python3
"""Module that defines a function inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
