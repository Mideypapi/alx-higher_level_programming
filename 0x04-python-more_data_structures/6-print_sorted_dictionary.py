#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for m, n in sorted(a_dictionary.items()):
        print("{}: {}".format(m, n))
