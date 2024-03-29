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

    def validate_attribute(self, key, value):
        """
        This method validates the attributes of a rectangle
        Raises Exceptions if they don't pass the validations
        """
        if type(value) is not int:
            raise TypeError(f'{key} must be an integer')

        if value <= 0 and key in ['width', 'height']:
            raise ValueError(f'{key} must be > 0')

        if value < 0 and key in ['x', 'y']:
            raise ValueError(f'{key} must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attribute('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attribute('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attribute('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attribute('y', value)
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
            properties = ('id', 'width', 'height', 'x', 'y')
            n_args = len(args)

            for i in range(n_args):
                key = properties[i]
                value = args[i]
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary with all the essential values
        """
        keys = ('id', 'width', 'height', 'x', 'y')
        result = {}

        for key in keys:
            value = getattr(self, key)
            result[key] = value

        return result

    def __str__(self):
        x, y, w, h = self.x, self.y, self.width, self.height
        return f'[Rectangle] ({self.id}) {x}/{y} - {w}/{h}'
