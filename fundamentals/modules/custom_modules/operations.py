# Module operations.py functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return None