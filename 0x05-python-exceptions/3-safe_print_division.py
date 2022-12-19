#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {}" .format(div))
        return (div)

    except (ZeroDivisionError, ValueError):
        print("Inside result: None")
        return (None)

    finally:
        print("", end="")
