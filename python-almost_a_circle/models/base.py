#!/usr/bin/python3
"""
Implements the base model
"""
from json import dumps, loads


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a passed dictionary to json string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f'{cls.__name__}.json'

        with open(filename, 'w') as f:
            if list_objs is not None:
                dicts = list(map(lambda obj: obj.to_dictionary(), list_objs))
            else:
                dicts = None

            json_data = cls.to_json_string(dicts)
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """
        Reads data from json string
        """
        if json_string is None:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new_obj = cls(5) if cls.__name__ == 'Square' else cls(5, 4)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        file_name = f'{cls.__name__}.json'
        try:
            with open(file_name, 'r') as f:
                json_data = f.read()
                objs = cls.from_json_string(json_data)
                return list(map(lambda obj: cls.create(**obj), objs))
        except:
            # Runs if the file does not exist
            return []
