#!/usr/bin/python3
"""Using unittest to create, well, unit tests"""
import unittest
mi = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests class"""

    def test_simple_case(self):
        """5 positive integers, no-repetitions"""
        self.assertEqual(mi([1, 2, 3, 4, 5]), 5)

    def test_negative_case(self):
        """5 negative integers, no-repetitions"""
        self.assertEqual(mi([-5, -4, -3, -2, -1]), -1)

    def test_randomly_sorted_case(self):
        """Randomly sorted integers"""
        self.assertEqual(mi([1, 2, 5, 3, 4]), 5)

    def test_repetitions_case(self):
        """Case where there is a repeated max"""
        self.assertEqual(mi([1, 2, 3, 4, 5, 5]), 5)

    def test_single_element_case(self):
        """"Just one element"""
        self.assertEqual(mi([5]), 5)

    def test_empty_list_case(self):
        """Empty list"""
        self.assertEqual(mi([]), None)
