#!/usr/bin/python3
"""3-write_file.py - Write to a file"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written

    ARGS:
        filename: file txt
        text: text to add to filename
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
