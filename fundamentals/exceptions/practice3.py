# Exercise 9 First valid answer
# Write a function that receives a list of texts, which simulate the answers of a user,
# and returns the first one that is a valid positive integer, converted to int.
# If none of them is valid, raise a ValueError with the message "No valid answer".
# Example: ["abc", "-3", "7", "2"] should return 7.

print("--- Exercise 9 ---\n")

def validate(data):
    for value in data:
        try:
            positive_integer = int(value)
        except ValueError:
            continue
        else:
            if positive_integer > 0:
                return positive_integer
    raise ValueError("No valid answer")

info = ["abc", "-3", "7", "2"]
countries = ["Mexico", "USA", "Canada"]

try:
    print(validate(info))
except ValueError as e:
    print(e)

try:
    print(validate(countries))
except ValueError as e:
    print(e)        

# Exercise 10 Safe call
# Write a function that receives a function and one argument, and calls the function with that argument.
# It returns a tuple (result, error_message): (result, None) if the call worked,
# or (None, message) if it raised an error, where message is the text of that error.
# Test it with int("42"), int("abc") and a lambda that divides by zero.

print("\n--- Exercise 10 ---\n")

def safe_call(func, arg):
    try:
        result = func(arg)
    except (ValueError, ZeroDivisionError, TypeError) as e:
        return None, str(e)
    else:
        return result, None

print(safe_call(int, "42"))  
print(safe_call(int, "abc"))

divided_by_zero = lambda x: x / 0
print(safe_call(divided_by_zero, 777))

# Exercise 11 Bank withdrawal
# Write a function that receives a balance and an amount, and returns the new balance after the withdrawal.
# If the amount is zero or negative, raise a ValueError with the message "Amount must be positive".
# If the amount is greater than the balance, raise a ValueError with the message "Insufficient funds".
# Test it with a valid withdrawal and one case for each error, printing the message of each error.

print("\n--- Exercise 11 ---\n")

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    print(withdraw(1000, 800))
except ValueError as e:
    print(e)

try:
    print(withdraw(1000, 4750))
except ValueError as e:
    print(e)

try:
    print(withdraw(1000, 0))
except ValueError as e:
    print(e)

# Exercise 12 Nested lookup
# Write a function that receives a dictionary of users, a username and a field name, and returns that field of that user.
# If the user does not exist, return "User not found". If the user exists but the field does not, return "Field not found".
# Example: with {"max": {"age": 20}}, ("max", "age") returns 20, ("ana", "age") returns "User not found"
# and ("max", "city") returns "Field not found".

print("\n--- Exercise 12 ---\n")

def lookup(users_dict, username, field_name):
    try:
        user = users_dict[username]
    except KeyError:
        return "User not found"
    try:
        return user[field_name]
    except KeyError:
        return "Field not found"

data = {"Max": {"age": 20}, 
        "Mildred": {"age": 18},
        "John": {"age": 32}}

print(lookup(data, "Max", "age"))
print(lookup(data, "Juan", "age"))
print(lookup(data, "Mildred", "height"))