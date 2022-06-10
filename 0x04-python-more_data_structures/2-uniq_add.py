#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    for i in range(0, len(my_list)):
        if my_list[result] in my_list[my_list[result]:]:
            my_list.pop(result)
    return sum(my_list)
