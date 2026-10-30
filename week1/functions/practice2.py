# Exercise 5 Price tag
# Write a function that receives item, price, and an optional currency that defaults to "MXN",
# and returns a string in the format "Coffee: 45.00 MXN".
# Call it once with positional arguments and once with keyword arguments.

print("--- Exercise 5 ---\n")

def string_format(item, price, currency="MXN"):
    return f"{item}: {price:.2f} {currency}"

print(string_format("MacBook Pro", 1699, "DLS"))
print(string_format(price=399, item="AirPods 4"))

# Exercise 6 Vowel counter
# Write a function that receives a text and returns how many vowels it contains.
# Uppercase and lowercase vowels should both count.
# Example: counting the vowels in "Hello World" should return 3.

print("\n--- Exercise 6 ---\n")

def total_vowels(text):
    return sum(1 for letter in text.lower() if letter in "aeiou")

print(total_vowels("Hello World"))
print(total_vowels("My name is Max"))
print(total_vowels("HAVE A NICE DAY"))

# Exercise 7 Discount calculator
# Write a function that receives a price and a discount percentage, and returns the price after the discount.
# If the percentage is greater than 100, return 0.
# Example: a price of 200 with a 25 percent discount should return 150.0.

print("\n--- Exercise 7 ---\n")

def calculate_price(price, discount):
    if discount > 100:
        return 0
    return round(price * (1 - discount / 100), 2)

print(calculate_price(3000, 50))
print(calculate_price(1299, 100))

# Exercise 8 Number summary
# Write a function that receives any number of numbers and returns 
# the count, the largest, and the smallest.
# If no numbers are given, return None.

print("\n--- Exercise 8 ---\n")

def number_summary(*numbers):

    if not numbers:
        return None

    count = 0
    largest = numbers[0] 
    smallest = numbers[0]

    for n in numbers:
        count += 1
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    return count, largest, smallest

print(number_summary(24, 63, 23))
print(number_summary())