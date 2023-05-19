#!/bin/usr/python3

a = 10
b = 5


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    resultA = add(a, b)
    resultM = mul(a, b)
    resultD = div(a, b)
    resultS = sub(a, b)

    print("{} + {} = {}".format(a, b, resultA))
    print("{} * {} = {}".format(a, b, resultM))
    print("{} / {} = {}".format(a, b, resultD))
    print("{} - {} = {}".format(a, b, resultS))
