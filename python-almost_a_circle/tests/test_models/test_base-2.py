#!/usr/bin/python3
"""Rectangle tests"""

from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase
import os

class TestRectangle(TestCase):
    """Class to test the Rectangle class"""

    def test_instance(self):
        """method name is self-explanatory"""
        
        # Checking automatic id assignment
        Base._Base__nb_objects = 0
        self.assertEqual(Rectangle(1, 1).id, 11)
        self.assertEqual(Rectangle(1, 1, 1).id, 2)
        self.assertEqual(Rectangle(1, 1, 1, 1).id, 3)

        # Checking manual id assignment
        self.assertEqual(Rectangle(1, 1, 1, 1, 4).id, 4)

        # Checking if the correct exceptions are raised
        # Also checking the messages of the exceptions
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "1")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "1")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "1")

    def test_area(self):
        """Test area calculation method"""
        self.assertEqual(Rectangle(10, 5).area(), 50)

    def test___str__(self):
        """Test str representation method"""
        self.assertEqual(str(Rectangle(10, 5)), "[Rectangle] (1) 0/0 - 10/5")

    def test_display(self):
        """Test the display method"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2, 3)
        r3 = Rectangle(3, 3, 4, 4)

        with patch("sys.stdout", new=StringIO()) as d:
            r1.display()
            self.assertEqual(d.getvalue(), "#\n")

        with patch("sys.stdout", new=StringIO()) as d:
            r2.display()
            self.assertEqual(d.getvalue(), "   ##\n   ##\n")

        with patch("sys.stdout", new=StringIO()) as d:
            r3.display()
            self.assertEqual(d.getvalue(), "\n\n\n\n    ###\n    ###\n    ###\n")

    def test_to_dictionary(self):
        """Test for the dic """
        Base._Base__nb_objects = 0
        self.assertEqual(Rectangle(1, 1).to_dictionary(), { 'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0 })

    def test_update(self):
        """test for the string"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 5)

        r.update()
        self.assertEqual(str(r), '[Rectangle] (1) 0/0 - 10/5')

        r.update(2)
        self.assertEqual(str(r), '[Rectangle] (2) 0/0 - 10/5')

        r.update(3, 4)
        self.assertEqual(str(r), '[Rectangle] (3) 0/0 - 4/5')

        r.update(5, 6, 7)
        self.assertEqual(str(r), '[Rectangle] (5) 0/0 - 6/7')

        r.update(8, 9, 10, 11)
        self.assertEqual(str(r), '[Rectangle] (8) 11/0 - 9/10')

        r.update(12, 13, 14, 15, 16)
        self.assertEqual(str(r), '[Rectangle] (12) 15/16 - 13/14')

        r.update(**{'id': 1})
        self.assertEqual(str(r), '[Rectangle] (1) 15/16 - 13/14')

        r.update(**{'id': 11, 'width': 12, 'height': 13, 'x': 14, 'y': 15})
        self.assertEqual(str(r), '[Rectangle] (11) 12/13 - 14/15')

    def test_create(self):
        """Tests to creatr a new rectangle"""

        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1 = Rectangle.create(**{'id': 89, 'width': 1,
                                 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_save_to_file(self):
        """Test for the save to save to file"""
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "width": 1, '
                             '"height": 2, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        """Test for the saving to a an empty file"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")
            self.assertEqual(type(file.read()), str)

    def test_load_from_file(self):
        """test geting a file form file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        from_file = Rectangle.load_from_file()
        self.assertEqual(type(from_file), list)
        self.assertEqual(from_file[0].width, 1)
        self.assertEqual(from_file[0].height, 2)
