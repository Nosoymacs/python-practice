# Exercise 5 Number parser
# Write a function that receives a list of texts and returns 
# a list with the ones that are valid integers, converted to int.
# The invalid texts are skipped. Example: ["1", "x", "3", "4.5"] should return [1, 3].

print("--- Exercise 5 ---\n")

def number_parser(data):
    valid_integers = []
    for value in data:
        try:
            number = int(value)
        except ValueError:
            continue
        else:
            valid_integers.append(number)
    return valid_integers

info = ["Max", "20", "GDL", "3.1416", "777"]
print(number_parser(info))

# Exercise 6 Basic calculator
# Write a function that receives two numbers and an operator +,-,*,/ and returns the result.
# If the operation divides by zero, return None.
# If the operator is not one of the four, raise a ValueError with the message "Unsupported operator".
# Test every case, including both errors, without letting the program stop.

print("\n--- Exercise 6 ---\n")

def calculator(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        try:
            return n1 / n2
        except ZeroDivisionError:
            return None
    else:
        raise ValueError("Unsupported operator")

try:
    print(calculator(4, 6, "+"))
except ValueError as e:
    print(e)

try:
    print(calculator(10, 8, "-"))
except ValueError as e:
    print(e)

try:
    print(calculator(200, 10, "*"))
except ValueError as e:
    print(e)

try:
    print(calculator(174, 6, "/"))
except ValueError as e:
    print(e)

try:
    print(calculator(300, 0, "/"))
except ValueError as e:
    print(e)

try:
    print(calculator(4, 6, "Hello World"))
except ValueError as e:
    print(e)

# Exercise 7 Age validator
# Write a function that receives a text and returns the age as an integer.
# If the text is not a number, raise a ValueError with the message "Age must be a number".
# If the age is negative or greater than 120, raise a ValueError with the message "Age out of range".
# Test it with a valid age and one case for each error, printing the message of each error.

print("\n--- Exercise 7 ---\n")

def validate(data):
    try:
        age = int(data)
    except ValueError:
        raise ValueError("Age must be a number")
    if age < 0 or age > 120:
        raise ValueError("Age out of range")
    return age
        
try:
    print(validate("20"))
except ValueError as e:
    print(e)

try:
    validate("Max")
except ValueError as e:
    print(e)

try:
    print(validate("-5312"))
except ValueError as e:
    print(e)

try:
    print(validate("249"))
except ValueError as e:
    print(e)

# Exercise 8 Conversion report
# Write a function that receives a text and returns it as an integer, or None if it is not a valid integer.
# Whatever the result, the function must always print "Conversion attempted" before it finishes.
# Test it with one valid and one invalid text.

print("\n--- Exercise 8 ---\n")

def conversion(data):
    try:
        return int(data)
    except ValueError:
        return None
    finally:
        print("Conversion attempted")

print(conversion("10"))
print(conversion("Bye World"))