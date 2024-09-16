#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    for _ in my_list:
        count += 1
    if idx < 0 or idx >= count:
        return my_list

    else:
        my_list[idx] = element
        return my_list
