#!/usr/bin/python3

a = 1
b = 2

if __name__ == "__main__":
    from add_0 import add

    retval = add(a, b)
    print("{} + {} = {}".format(a, b, retval))
