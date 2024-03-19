#!/usr/bin/python3
"""12-student.py - Student to JSON with filter"""


class Student:
    """class Student that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None):
        that retrieves a dictionary representation of a
        Student instance (same as 10-class_to_json.py):
            If attrs is a list of strings, only attribute
            names contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
