#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import pep8
import json
import os
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    def test_id(self):
        """Test given ids"""
        self.assertTrue(Base(98), self.id == 98)
        self.assertTrue(Base(9), self.id == 9)
        self.assertTrue(Base(8), self.id == 8)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_auto(self):
        """Test id when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    """Test Class to JSON string."""
    def test_to_json_string(self):
        """Test dict given translates into JSON string"""
        rect1 = {"id": 1, "width": 9, "height": 8, "x": 98, "y": 89}
        rect2 = {"id": 21, "width": 29, "height": 28, "x": 298, "y": 289}
        str_rect = Base.to_json_string([rect1,rect2])
        self.assertTrue(str_rect,
                        [{"id": 1, "width": 9, "height": 8, "x": 98, "y": 89},
                         {"id": 21, "width": 29, "height": 28, "x": 298, "y": 289}])

    def test_to_json_string_empty(self):
        """Test empty dict given translates into JSON string of empty dict"""
        dict1 = dict()
        str_dict = Base.to_json_string([dict1])
        self.assertTrue(type(str_dict) == str)
        self.assertTrue(str_dict, "[]")

    """Test JSON string to Class."""
    def test_from_json_string(self):
        """Test JSON string to dictionary."""
        str_rect = '[{"id": 1, "width": 9, "height": 8, "x": 98, "y": 89},\
               {"id": 21, "width": 29, "height": 28, "x": 298, "y": 289}]'
        list_rect = Base.from_json_string(s0)
        self.assertTrue(type(str_rect) == str)
        self.assertTrue(type(dict_rect) == list)
        self.assertTrue(type(list_rect[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 1, "width": 9, "height": 8, "x": 98, "y": 89},
                         {"id": 21, "width": 29, "height": 28, "x": 298, "y": 289}])

    def test_from_empty_json_string(self):
        """Test an empty JSON string to dictionary list."""
        str1 = ""
        str2 = Base.from_json_string(str1)
        self.assertTrue(type(str2) == list)
        self.assertTrue(str2 == [])

    def test_create(self):
        """Test creating object from dictionary list."""
        rect1 = Rectangle(9, 8, 98, 89, 1)
        dict1 = rect1.to_dictionary()
        dict2 = Rectangle(29, 28, 298, 289, 21)
        rect2 = Rectangle.create(**dict2)
        self.assertEqual(str(rect1), '[Rectangle] (1) 98/89 - 9/8')
        self.assertEqual(str(rect2), '[Rectangle] (21) 298/289 - 29/28')

    def test_save_to_file(self):
        """Test save to file"""
        rect1 = Rectangle(9, 8, 98, 89, 1)
        rect2 = Rectangle(29, 28, 298, 289, 21)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([rect1.to_dictionary(), rect2.to_dictionary()]),
                file.read())

    def test_load_from_file(self):
        """Test load from file"""
        rect1 = Rectangle(9, 8, 98, 89, 1)
        rect2 = Rectangle(29, 28, 298, 289, 21)
        Rectangle.save_to_file([rect1, rect2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (1) 98/89 - 9/8')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (21) 298/289 - 29/28')
