# Exercise 1 Temperature converter
# Write a function that takes a temperature in degrees Celsius
# and returns its equivalent in degrees Fahrenheit.

print("--- Exercise 1 ---\n")

def celsius_to_fahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2)

print(celsius_to_fahrenheit(30))
print(celsius_to_fahrenheit(26))

# Exercise 2 Age check
# Write a function that returns True if the age is 18 or older, and False otherwise.

print("\n--- Exercise 2 ---\n")

def age_check(age):
    return age >= 18

print(age_check(26))
print(age_check(9))

# Exercise 3 Full name 
# Write a function that returns the full name. 
# If no last name is given, return only the first name.

print("\n--- Exercise 3 ---\n")

def full_name(first_name, last_name=None):
    if not last_name:
        return first_name
    return f"{first_name} {last_name}"

print(full_name("Mildred"))
print(full_name("Mildred", ""))
print(full_name("Max", "Gonzalez"))

# Exercise 4 Average of three
# Write a function that returns the average of three numbers

print("\n--- Exercise 4 ---\n")

def average_of_three(n1, n2, n3):
    return round((n1 + n2 + n3) / 3, 2)

print(average_of_three(10, 10, 10))
print(average_of_three(100, 2400, 33))
