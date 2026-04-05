#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        self.assertIsNone(max_integer())

    def test_max_float(self):
        self.assertEqual(max_integer([1.2, 2.5, 3.1]), 3.1)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)

    def test_same_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

