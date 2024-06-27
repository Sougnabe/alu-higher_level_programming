#!/usr/bin/python3
def fin(my_list=[]):
    if isinstance(my_list, list):
        count = len(my_list) - 1
        if count >= 0:
            for i in my_list:
                print("{:d}".format(my_list[count]))
                count -= 1
