#!/usr/bin/python3
"""writes into a file"""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8") as f:
        write_file = f.write(text)
        return f.write(text)
