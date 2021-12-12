#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_documentation_module(self):
        """Tests for module documentation"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 10)

    def test_documentation_function(self):
        """Tests for funstion documentation"""
        self.assertTrue(len(max_integer.__doc__) > 10)

    def test_normal_list(self):
        """Tests for normal operation"""
        lst = [1, 2, 3, 4, 98]
        self.assertEqual(max_integer(lst), 98)

    def test_one_elem(self):
        """Tests for only one element in the list"""
        lst = [98]
        self.assertEqual(max_integer(lst), 98)

    def test_max_middle(self):
        """Tests with max in the middle"""
        lst = [1, 2, 98, 4, 5]
        self.assertEqual(max_integer(lst), 98)

    def test_with_negative(self):
        """Tests with negative element"""
        on = [-1, 2, 3, 4, 98]
        self.assertEqual(max_integer(on), 98)

    def test_non_int(self):
        """Tests for a non int in list"""
        string = ["Hello", 1, 2, 4]
        with self.assertRaises(TypeError):
            max_integer(string)


if __name__ == "__main__":
    unittest.main()
