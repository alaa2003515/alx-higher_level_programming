#!/usr/bin/python3
import sys

# Two blank lines here


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        result = True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        result = False
    return result
