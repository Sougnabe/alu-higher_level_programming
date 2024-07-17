#!/usr/bin/python3
'''a python script which read a file'''
def read_file(filename=""):
    """reads the file given"""
    with open(filename, encodng="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
