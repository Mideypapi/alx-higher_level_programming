#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletion of keys with a specific val in a dic."""
    while value in a_dictionary.values():
        for m, x in a_dictionary.items():
            if x == value:
                del a_dictionary[m]
                break

    return (a_dictionary)
