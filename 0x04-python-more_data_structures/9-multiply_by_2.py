#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for m, n in new_dictionary.items():
        n = n * 2
        new_dictionary[m] = n
    return (new_dictionary)
