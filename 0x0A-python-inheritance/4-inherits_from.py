#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
4-inherits_from.py: Only sub class of
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False."""
    if issubclass(a_class, obj.__class__) is False and \
       isinstance(obj, a_class):
        return True
    return False
