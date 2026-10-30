# Exercise 9 Profile builder
# Write a function that receives any number of keyword arguments and returns them as a dictionary.
# Then write a second function that receives that dictionary 
# and prints each key and value on its own line.

print("--- Exercise 9 ---\n")

def profile_builder(**data):
    return data

def show_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

profile = profile_builder(name="Max", age=20, city="GDL")
show_dictionary(profile)

# Exercise 10 Function composition
# Write a function that receives two functions, f and g, and returns a new function.
# The new function should apply g to a value, then apply f to the result.
# Test it with two functions of your own.

print("\n--- Exercise 10 ---\n")

divided_by_4 = lambda x: x/4
pow_5 = lambda x: x**5

def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

pow_then_divide = compose(divided_by_4, pow_5)
print(pow_then_divide(10))

# Exercise 11 Multiplier factory
# Write a function that receives a number n and returns a new function.
# The new function receives a number and returns it multiplied by n.
# Example: create a triple function with n = 3, then calling it with 5 should return 15.

print("\n--- Exercise 11 ---\n")

def multiplier(n):
    def multiply(x):
        return n * x
    return multiply

triple = multiplier(3)
print(triple(5))

# Exercise 12 Calculator with operations
# Write a function that receives two numbers and an operation, 
# which is a function that takes two numbers, 
# and returns the result of applying the operation to them.
# Test it with at least three different operations, including one lambda.

print("\n--- Exercise 12 ---\n")

add = lambda x, y: x + y
subtraction = lambda x, y: x - y
product = lambda x, y: x * y

def calculator(n1, n2, operation):
    return operation(n1, n2)

print(calculator(10, 2, add))
print(calculator(10, 2, subtraction))
print(calculator(10, 2, product))