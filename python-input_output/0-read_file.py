#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encodng="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
