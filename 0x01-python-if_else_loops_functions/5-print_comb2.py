#!/usr/bin/python3

for val in range(100):
    if val == 99:
        print("{}".format(val))
    else:
        print("{:02}".format(val), end=', ')
