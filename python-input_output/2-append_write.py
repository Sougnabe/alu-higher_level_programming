#!/usr/bin/python3
"""add text in file"""


def append_write(filename="", text=""):
    """add text in file"""
    with open(filename, '+a') as f:
        return f.write(text)
