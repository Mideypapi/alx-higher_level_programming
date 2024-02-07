#!/usr/bin/python3
"""6-from_json_string.py - From JSON string to Object"""


import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string

    ARGS:
        my_str: JSON string
    Return:
        an object (Python data structure)
    """
    return json.loads(my_str)
