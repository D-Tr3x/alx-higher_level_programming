#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = 0
    for i in my_list:
        count += 1
    if idx < 0 or idx >= count:
        return my_list
    else:
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
