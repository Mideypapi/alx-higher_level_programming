#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
0-lookup.py: returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Return list attributes """
    return dir(obj)
