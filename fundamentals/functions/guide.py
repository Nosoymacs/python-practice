# Python reference functions

# 1. BASIC FUNCTION
# A function is a reusable block of code.
# Use 'def' to define a function.

def greet(name):
    return f"Hello, {name}!"

print(greet("Max"))  # Hello, Max!

# 2. RETURN VS PRINT
# print() displays information on the screen.
# return sends a value back to the caller.

def double(n):
    return n * 2

result = double(4)
print(result + 1)  # 9

# A function without an explicit return statement
# returns None by default.

def no_return(n):
    print(n)

value = no_return(5)  # Prints 5
print(value)          # None

# 3. PARAMETERS AND DEFAULT VALUES
# A default parameter value is used when the caller
# does not provide an argument for that parameter.

def add(a, b=0):
    return a + b

print(add(3, 4))  # 7
print(add(10))    # 10

# 4. KEYWORD ARGUMENTS
# Keyword arguments specify parameters by name.
# Their order does not matter when all arguments are named.

def introduce(name, city="Guadalajara"):
    return f"My name is {name} and I live in {city}."

print(introduce("Max"))
print(introduce(city="Monterrey", name="Luis"))

# 5. LOCAL VS GLOBAL VARIABLES
# A local variable belongs to the function where it is defined.
# Assigning a value to a local variable does not change
# a global variable with the same name.

counter = 0

def increment():
    counter = 1
    return counter

increment()
print(counter)  # 0

# 6. STRING JOIN
# str.join() combines strings from an iterable
# using the string before '.join()' as a separator.

names = ("Ana", "Luis", "Max")

print(", ".join(names))  # Ana, Luis, Max

# 7. *ARGS
# *args collects any number of positional arguments
# into a tuple.

def show(*names):
    print(names)

show("Ana", "Luis")  # ('Ana', 'Luis')
show()               # ()

# *args can also be used to process multiple numbers.

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))  # 6
print(total())         # 0

# 8. **KWARGS
# **kwargs collects any number of keyword arguments
# into a dictionary.

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


describe(name="Max", city="Guadalajara")

# Output:
# name: Max
# city: Guadalajara

# 9. FUNCTIONS CALLING FUNCTIONS
# A function can call another function to reuse its logic.

def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))  # 25

# 10. LAMBDA FUNCTIONS
# A lambda is a small anonymous function consisting
# of a single expression.

double_lambda = lambda x: x * 2

print(double_lambda(5))  # 10

def double_def(x): # The equivalent function using 'def'
    return x * 2

# 11. DOCSTRINGS
# A docstring documents what a function does.
# It is written as the first statement inside the function.

def square_doc(n):
    """Return the square of a number."""
    return n * n

print(square_doc.__doc__)  # Return the square of a number.

# 12. FUNCTIONS AS ARGUMENTS
# Functions are first-class objects in Python.
# This means a function can be passed to another function as an argument.

def shout(text):
    return text.upper()

def apply(func, value):
    return func(value)

print(apply(shout, "hello"))  # HELLO