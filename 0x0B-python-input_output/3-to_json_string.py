#!/usr/bin/python3
"""5-to_json_string.py - To JSON string """


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)
    ARGS:
        my_obj: object to be serialized
    """
    return json.dumps(my_obj)
