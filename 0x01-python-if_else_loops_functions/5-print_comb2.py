#!/usr/bin/python3

for val in range(100):
    if val == 99:
        print(f"{val}")
    else:
        print(f"{val:02}", end=', ')
