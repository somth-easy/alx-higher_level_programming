#!/usr/bin/python3

def uppercase(str):

    new_str = ""

    for char in str:

        if 'A' <= char <= 'Z':
            new_str += char
            continue
        elif 'a' <= char <= 'z':
            new_str += chr(ord(char) - 32)
        else:
            new_str += char

    print(new_str)
