#!/usr/bin/python3
"""7-save_to_json_file.py - Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation
    ARGS:
        my_obj: object to write in a text file
        filename: text file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
