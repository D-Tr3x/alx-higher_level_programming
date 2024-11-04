#!/usr/bin/python3
""" Unit tests for Base class in Almost a Circle
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class """

    def setUp(self):
        """ Resets Base ID for each test """
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """ Test for automatic ID increment  """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """ Test for custom ID assignment"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_auto_after(self):
        """ Test for incrementing after a custom ID """
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()
