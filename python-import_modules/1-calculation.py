#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    num1 = add(a, b)
    num2 = sub(a, b)
    num3 = mul(a, b)
    num4 = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, num1))
    print("{:d} - {:d} = {:d}".format(a, b, num2))
    print("{:d} * {:d} = {:d}".format(a, b, num3))
    print("{:d} / {:d} = {:d}".format(a, b, num4))
