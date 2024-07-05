#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print(my_list[count], end='')
            count += 1
        except IndexError:
            pass
        finally:
            print()
            return count
print(safe_print_list([1, 2, 3, 4], 4))
print(safe_print_list([1, 2, 3, 4], 2))
print(safe_print_list([1, 2, 3, 4], 0))
print(safe_print_list([], 0))
print(safe_print_list([1, 2, 3, 4], 5))
print(safe_print_list([1, 2, 3, 4], 14))
