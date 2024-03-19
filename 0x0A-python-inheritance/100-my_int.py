#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
100-my_int.py: My integer
"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
