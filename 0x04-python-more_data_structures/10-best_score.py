#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    to_return = list(a_dictionary.keys())[0]
    big = a_dictionary[to_return]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            to_return = k
    return (to_return)
