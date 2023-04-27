#!/usr/bin/python3
"""
Implements the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class which inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        x, y, w, id = self.x, self.y, self.width, self.id
        return f'[Square] ({id}) {x}/{y} - {w}'