#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        for n in range(len(my_list)):
            if n == idx:
                return my_list[n]
