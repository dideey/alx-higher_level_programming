#!/usr/bin/python3

"""
Base class module.

This module defines the Base class.
"""

import json


class Base:
    """
    Base class is the base class for other classes.

    Attributes:
        nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        objects_list = []

        if list_objs is not None and len(list_objs) > 0:

            for instance in list_objs:

                objects_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:

            f.write(cls.to_json_string(objects_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)
