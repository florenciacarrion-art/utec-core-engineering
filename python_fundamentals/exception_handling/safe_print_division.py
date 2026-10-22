#!/usr/bin/env python3

def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        result = None
    finally:
        print("Inside resulr:{}".format(result))
    return result
