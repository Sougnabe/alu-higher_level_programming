#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
for x in dir(variable_load_5):
    if x[0] == "a":
        print("{:s}".format(x))
