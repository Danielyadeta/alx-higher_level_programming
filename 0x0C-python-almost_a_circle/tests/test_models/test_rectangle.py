#!/usr/bin/python3
"""
Unittest for Rectangle Class.
"""
import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    def test_attr(self):
        """Test all given attributes"""
        r1 = Rectangle(9, 8, 98, 89, 1)
        self.assertTrue(r1.width == 9)
        self.assertTrue(r1.height == 8)
        self.assertTrue(r1.x == 98)
        self.assertTrue(r1.y == 89)
        self.assertTrue(r1.id == 1)

    def test_validations(self):
        """Test attribute validations"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"d": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -99, 1)

    def test_area(self):
        """Test area"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_str(self):
        """Test __str__"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test update"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')

    def test_to_dictionary(self):
        """Test to_dictionary"""
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
