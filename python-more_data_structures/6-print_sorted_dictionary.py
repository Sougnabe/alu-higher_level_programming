#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for temp in sorted_dictionary:
        print("{}: {}".format(temp, a_dictionary[temp]))
