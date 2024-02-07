#!/usr/bin/python3
"""10-class_to_json.py - Class to JSON"""


def class_to_json(obj):
    """function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    ARGS:
        obj: is an instance of a Class
    Return:
        the dictionary description with simple data structure
    """
    return obj.__dict__
