#!/usr/bin/python3
""" Unit tests for Base class in Almost a Circle """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class """

    def setUp(self):
        """ Resets Base ID for each test """
        Base._Base__nb_objects = 0

    def test_default(self):
        """ Test with default values """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_auto_id(self):
        """ Test for automatic ID increment """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """ Test with customized ID assigned """
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_auto_id_after_custom(self):
        """ Test with default values """
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 2)

    def test_to_json_none(self):
        """ Test to_json_string with `None` """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty_list(self):
        """ Test to_json_string with `empty list` """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_single_dict(self):
        """ Test to_json_string with dictionary with single value """
        self.assertEqual(Base.to_json_string([{'id': 33}]), '[{"id": 33}]')

    def test_to_json_default(self):
        """ Test to_json_string with valid dictionary """
        list_dictionary = [{'id': 1, 'width': 2, 'height': 4}]
        json_string = Base.to_json_string(list_dictionary)
        self.assertEqual(json_string, '[{"id": 1, "width": 2, "height": 4}]')

    def test_to_json_returns_string(self):
        """ Test that to_json_string returns a string """
        json_str = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_str, str)

    def test_from_json_none(self):
        """ Test from_json_string with `None` """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty_(self):
        """ Test from_json_string with `empty string` """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_default(self):
        """ Test from_json_string with valid JSON string """
        json_string = '[{"id": 1, "x": 2, "y": 2}]'
        dictionary = Base.from_json_string(json_string)
        self.assertEqual(dictionary, [{'id': 1, 'x': 2, 'y': 2}])

    def test_from_json_returns_list(self):
        """ Test that from_json_string returns a list """
        json_str = '[{"id": 12}]'
        data = Base.from_json_string(json_str)
        self.assertIsInstance(data, list)



if __name__ == '__main__':
    unittest.main()
