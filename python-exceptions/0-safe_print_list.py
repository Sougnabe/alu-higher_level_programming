#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("class[x:d]")
    except TypeError:
        print("class[x:s]")
    except TypeError:
        print("class[x:f]")

