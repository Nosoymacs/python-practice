# Exercise 7 Calculator in two modules
# Create a module called operations.py with four functions that receive two numbers each: add, subtract,
# multiply and divide. If the division is by zero, return None.
# Create a second module called calculator.py that imports operations and has a function that receives
# two numbers and an operator ("+", "-", "*" or "/") and returns the result, using the functions of
# operations. If the operator is not one of the four, raise a ValueError with the message
# "Unsupported operator".
# Import only calculator and test it, including both error cases.

print("\n--- Exercise 7 ---\n")

import calculator

print(f"21 + 75 = {calculator.calculate(21, 75, "+")}")  # 96
print(f"43 - 23 = {calculator.calculate(43, 23, "-")}")  # 20
print(f"12 * 7 = {calculator.calculate(12, 7, "*")}")    # 84
print(f"10 / 5 = {calculator.calculate(10, 5, "/")}")    # 2
print(f"99 / 0 = {calculator.calculate(99, 0, "/")}")    # None

try:
    print(f"99 & 0 = {calculator.calculate(99, 0, "&")}")    # Unsupported operator
except ValueError as e:
    print(e)