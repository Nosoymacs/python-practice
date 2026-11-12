# Module calculator.py functions

import operations

def calculate(n1, n2, operator):
    if operator == "+":
        return operations.add(n1, n2)
    elif operator == "-":
        return operations.subtract(n1, n2)
    elif operator == "*":
        return operations.multiply(n1, n2)
    elif operator == "/":
        return operations.divide(n1, n2)
    raise ValueError("Unsupported operator")