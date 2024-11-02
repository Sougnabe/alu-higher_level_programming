#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    values = sys.argv
    length = len(values)
    i = 1
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(values[1]))
    elif length > 2:
        print("{:d} arguments:".format(length-1))
        while i < length:
            print("{:d}: {}".format((i), values[i]))
            i = i + 1
