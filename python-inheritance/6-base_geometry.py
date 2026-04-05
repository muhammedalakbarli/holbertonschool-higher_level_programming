#!/usr/bin/python3
"""Module that defines BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise exception since area is not implemented."""
        raise Exception("area() is not implemented")
