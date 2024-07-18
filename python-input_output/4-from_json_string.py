#!/usr/bin/python3
"""script which returns an object (Python data structure) represented by a JSON string"""


import json


def from_json_string(my_str):
    """function that returns an object (Python data structure) represented by a JSON string:"""
    return json.dumbs(my_str)
