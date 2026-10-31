# Exercise 1 Safe integer conversion
# Write a function that receives a text and returns it as an integer.
# If the text is not a valid integer, return None.
# Example: "76" should return 76, and "abc" should return None.

print("--- Exercise 1 ---\n")

def converter(text):
    try:
        return int(text)
    except ValueError:
        return None

print(converter("999"))
print(converter("zzz"))


# Exercise 2 Safe list access
# Write a function that receives a list and an index, and returns the item at that index.
# If the index does not exist in the list, return None.
# Example: with the list [10, 20, 30], index 1 returns 20 and index 5 returns None.

print("\n--- Exercise 2---\n")

def access(data, index):
    try:
        return data[index]
    except IndexError:
        return None

names = ["Max", "Mildred", "John"]

print(access(names, 0))
print(access(names, 7))

# Exercise 3 Dictionary lookup
# Write a function that receives a dictionary and a key, and returns the value for that key.
# If the key does not exist, return the text "Not found".
# Example: with {"name": "Max"}, the key "name" returns "Max" and the key "age" returns "Not found".

print("\n--- Exercise 3---\n")

def lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return "Not found"

ages = {"Max": 20, "Mildred": 18, "John": 33}

print(lookup(ages, "Mildred"))
print(lookup(ages, "Juan"))

# Exercise 4 Positive number validator
# Write a function that receives a number and returns it if it is positive.
# If the number is zero or negative, the function must raise a ValueError with the message "Number must be positive".
# Call it once with a valid value and once with an invalid one, and print the message of the error.

print("\n--- Exercise 4---\n")

def validate(number):
    if number > 0:
        return number
    else:
        raise ValueError("Number must be positive")

try:
    print(validate(33))
except ValueError as e:
    print(e)

try:
    print(validate(-5))
except ValueError as e:
    print(e)