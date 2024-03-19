#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
1-my_list.py: class MyList that inherits from d list
"""


class MyList(list):
    """class MyList that inherits from list and print"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        if issubclass(MyList, list):
            print(sorted(self))
