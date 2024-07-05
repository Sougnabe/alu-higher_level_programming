#!/usr/bin/python3
def safe_print_list(my_list=[], x):
    try:
        print("my_list[x:d]")
    except TypeError:
        print("my_list[x:s]")
    except TypeError:
        print("my_list[x:f]")

