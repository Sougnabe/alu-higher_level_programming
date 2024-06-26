#!/usr/bin/python3
if "__name__" == "__main__":
    import sys
    argv = sys.argv[1:] 
    arg_count = len(argv)

    if arg_count == 0:
        print("Number of argument(s): 0.")
    elif arg_count == 1:
        print("Number of argument(s): 1 argument:")
    else:
        print(f"Number of argument(s): {arg_count} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
