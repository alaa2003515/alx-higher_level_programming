#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            div_res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
        except (TypeError, IndexError):
            print("wrong type or out of range")
            div_res = 0
        finally:
            result_list.append(div_res)
    return result_list
