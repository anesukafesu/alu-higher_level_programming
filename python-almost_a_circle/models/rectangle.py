#!/usr/bin/python3
"""
Implements the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if type(value) is not int:
            raise TypeError(f'{key} must be an integer')

        if value <= 0 and (key == 'width' or key == 'height'):
            raise ValueError(f'{key} must be > 0')

        if value < 0 and (key == 'x' or key == 'y'):
            raise ValueError(f'{key} must be >= 0')

        if key in ['x', 'y', 'width', 'height']:
            self.__dict__['_Rectangle__' + key] = value
        else:
            self.__dict__[key] = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle using pound signs(#)"""
        print('\n' * self.y, end='')
        line = " " * self.x + "#" * self.width + "\n"
        rect = line * self.height
        print(rect.rstrip())

    def update(self, *args, **kwargs):
        """Updates properties passed in
        Should be passed in the order id, width, height, x, y
        """
        if len(args) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            properties = ('id', 'width', 'height', 'x', 'y')
            n_args = len(args)

            for i in range(n_args):
                key = properties[i]
                value = args[i]
                setattr(self, key, value)

    def __str__(self):
        x, y, w, h = self.x, self.y, self.width, self.height
        return f'[Rectangle] ({self.d}) {x}/{y} - {w}/{h}'
