#!/usr/bin/python3
"""writes into a file"""


def write_file(filename="", text=""):
    """write in file"""
    with open(filename, 'w+') as f:
        return f.write(text)
