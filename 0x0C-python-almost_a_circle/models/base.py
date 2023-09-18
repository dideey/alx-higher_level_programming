#!/usr/bin/python3

import json

class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """checking if id is none
            and assigning to it
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return ("[]")
        return  json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):


    @staticmethod
        def from_json_string(json_string):
            if json_string is None:
                x = []
                return x
            return json.loads(json_string)
