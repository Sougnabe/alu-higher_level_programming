#!/usr/bin/python3
def safe_print_list(my_list=[], x):
    count = 0
    while count < x:
        try:
            print('my_list[count]', end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
