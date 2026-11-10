# Exercise 1 Math helpers module
# Create a module called math_helpers.py with two functions: one that receives a number and returns
# its square, and one that receives a number and returns its cube.
# Import the module and use both functions.

print("--- Exercise 1 ---\n")

import math_helpers

numbers = [25, 64, 23, 81]

for n in numbers:
    print(f"Square of {n}: {math_helpers.square(n)}")

for n in numbers:
    print(f"Cube of {n}: {math_helpers.cube(n)}")


# Exercise 2 Constants module
# Create a module called settings.py with three variables: the name of an app, its version as text,
# and a maximum number of login attempts.
# Import only the name and the maximum attempts, and print one line that uses both.

print("\n--- Exercise 2 ---\n")

from settings import APP_NAME, MAX_LOGIN_ATTEMPTS

print(f"App {APP_NAME} allows a maximum of {MAX_LOGIN_ATTEMPTS} login attempts")

# Exercise 3 Squares with an alias
# Write a function that receives a list of numbers and returns a new list with the square of each one.
# It must use the module from Exercise 1, imported with a short alias.

print("\n--- Exercise 3 ---\n")

import math_helpers as mh

def squares(values):
    result = []
    for n in values:
        result.append(mh.square(n))
    return result

numbers = [25, 36, 64, 81]
print(squares(numbers))