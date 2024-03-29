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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Returns a dictionary object that represents this object
        """
        result = super().to_dictionary()
        result['size'] = result['width']
        del result['width']
        del result['height']
        return result

    def update(self, *args, **kwargs):
        """
        Update square values
        """
        if len(args) > 0:
            if len(args) > 1:
                # Duplicating the size value to become width and height
                args = args[0:2] + args[1:]
            super().update(*args)
        else:
            if 'size' in kwargs:
                # Converting size value to become width and height values
                kwargs['width'] = kwargs['height'] = kwargs['size']
                del kwargs['size']

            super().update(**kwargs)
