#!/usr/bin/python3
"""This module provides a function to print a text with indentation rules."""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""

    for ch in text:
        line += ch

        if ch in separators:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")
