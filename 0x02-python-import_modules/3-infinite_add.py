#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    retval = 0

    if argc == 0:
        print("{}".format(argc))
    elif argc == 1:
        print("{}".format(sys.argv[argc]))
    else:
        for i in range(1, argc + 1):
            retval += int(sys.argv[i])
        print("{}".format(retval))
