#!/usr/bin/python3
def uniq_add(my_list=[]):
    already = []
    sum = 0
    if my_list:
        for i in my_list:
            if i not in already:
                sum += i
                already.append(i)
    return sum
