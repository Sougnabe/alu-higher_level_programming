#!/usr/bin/python3


"""writes an Object to a text file, using a JSON representation:"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w+') as f:
        return f.dump(my_obj, f)
