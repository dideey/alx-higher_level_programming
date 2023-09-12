#!/usr/bin/python3
"""import the json"""


import json


def to_json_string(my_obj):
    """return string rep"""
    son = json.dumps(my_obj)
    return son
