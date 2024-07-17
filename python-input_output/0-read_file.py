#!/usr/bin/python3
'''a python script which read a file'''
def read_file(filename=""):
    """reads the file given"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
