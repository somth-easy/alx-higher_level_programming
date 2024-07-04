#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    lo = my_list1
    lt = my_list2
    new_list = []
    for i in range(list_length):
        try:
            val = lo[i] / lt[i]
        except IndexError:
            print("out of range")
            val = 0
        except ZeroDivisionError:
            print("division by 0")
            val = 0
        except TypeError:
            print("wrong type")
            val = 0
        finally:
            if isinstance(val, (int, float)):
                new_list.append(val)
    return new_list
