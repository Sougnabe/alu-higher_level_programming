#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    char = sys.argv
    leng = len(char)
    i = 1
    summ = 0
    if leng == 1:
        print("{:d}".format(summ))
    elif leng == 2:
        print("{:d}".format(char(values[1])))
    elif leng > 2:
        while i < leng:
            summ = summ + int(char[i])
            i = i + 1
        print("{:d}".format(summ))
