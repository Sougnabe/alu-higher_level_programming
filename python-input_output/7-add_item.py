#!/usr/bin/python3
"""adds all arguments to a Python list, and save in file"""

import os
import sys


from 5-save_to_json_file.py import save_to_json_fil
from 6-load_from_json_file.py import load_from_json_file


filename = "add_item.json"
try:
    # Load existing data from the file if it exists
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
except Exception:
    my_list = []

# Add all command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
