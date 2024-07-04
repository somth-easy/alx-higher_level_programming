#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        x = (a/b)
    except ZeroDivisionError:
        pass
    finally:
        if (b == 0):
            x = 'None'
        print("Inside result: {}".format(x))
        return x
