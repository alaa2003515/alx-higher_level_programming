#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    i = 5
    print("{} + {} = {}".format(a, i, add(a, i)))
    print("{} - {} = {}".format(a, i, sub(a, i)))
    print("{} * {} = {}".format(a, i, mul(a, i)))
    print("{} / {} = {}".format(a, i, div(a, i)))
