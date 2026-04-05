#!/usr/bin/python3
"""Module that defines a function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or inherited from it."""
    return isinstance(obj, a_class)
