#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):


    def test_empty(self):
        """ Test with an empty list """
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        """ Test with single item in the list """
        self.assertEqual(max_integer([9]), 9)

    def test_multiple(self):
        """ Test with multiple numbers in the list """
        self.assertEqual(max_integer([1, 3, 2, 5]), 5)

    def test_duplicate(self):
        """ Test with duplicate max numbers """
        self.assertEqual(max_integer([4, 8, 4, 5, 8]), 8)

    def test_negative(self):
        """ Test with negative numbers """
        self.assertEqual(max_integer([-9, -5, -1, -3]), -1)

    def test_float(self):
        """ Test with float numbers """
        self.assertEqual(max_integer([1.9, 5.5, 1.8, 3.7]), 5.5)

    def test_nint(self):
        """ Test with non-integer items (str) """
        with self.assertRaises(TypeError):
            max_integer([1, 'b', 3])

    def test_none(self):
        """ Test with None as item """
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_nlist(self):
        """ Test with non-list (str) """
        self.assertEqual(max_integer('alpha'), 'p')

if __name__ == '__main__':
    unittest.main()
