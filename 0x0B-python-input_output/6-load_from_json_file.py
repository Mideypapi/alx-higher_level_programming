#!/usr/bin/python3
"""8-load_from_json_file.py - Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file
    ARGS:
        filename: text file
    """
    with open(filename, encoding='utf-8') as a_file:
        return (json.load(a_file))
