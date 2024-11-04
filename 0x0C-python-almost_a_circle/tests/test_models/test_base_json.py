#!/usr/bin/python3
""" Unit tests for Base class JSON """

import unittest
from models.base import Base


class TestBaseJson(unittest.TestCase):
    """ Test cases for JSON in Base """

    def test_to_json_none(self):
        """ Test to_json_string with None """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty_list(self):
        """ Test to_json with an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_single(self):
        """ Test to_json with a list with only 1 dictionary item"""
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id: 12"}]')
        self.assertEqual(json_str, str)


    def test_from_json_none(self):
        """ Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty_list(self):
        """ Test from_json with an empty JSON list """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_single(self):
        """ Test from_json with a JSON string of one single dictionary item """
        json_list = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(json_list, [{'id': 89}])
        self.assertEqual(json_list, list)

if __name__ == '__main__':
    unittest.main()
