#!/usr/bin/python3

for i in range(10):
    for n in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, n))
            continue
        else:
            print("{}{}".format(i, n), end=', ')
