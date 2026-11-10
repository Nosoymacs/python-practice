# Exercise 4 Temperature module
# Create a module called temperature.py with two functions: one that converts Celsius to Fahrenheit and
# one that converts Fahrenheit to Celsius, both rounded to 1 decimal.
# When the file is run directly, it must print the conversions from 0 to 100 degrees Celsius in steps of 25.
# When the file is imported, it must print nothing.
# Import it and check that nothing extra is printed.

print("--- Exercise 4 ---\n")

import temperature

print(temperature.celsius_to_fahrenheit(0))  # 32
print(temperature.fahrenheit_to_celsius(32)) # 0

# Exercise 5 Random tools module
# Create a module called random_tools.py with two functions. The first one receives a list and returns
# two different random items of it; if the list has fewer than two items, it must raise a ValueError
# with the message "Not enough items". The second one receives a number of players and returns a list
# with that many random scores between 1 and 100.
# Import both functions and test them, including the error case.

print("\n--- Exercise 5 ---\n")

from random_tools import random_items, random_scores

cities = ["GDL", "Mexico City", "Cancun", "San Francisco"]
empty = []

print(random_items(cities))
try:
    print(random_items(empty))
except ValueError as e:
    print(e)

print(random_scores(4))
print(random_scores(10))

# Exercise 6 Date tools module
# Create a module called date_tools.py with the calculate_age and days_left functions from your modules
# exercises, plus a third function that receives a year, a month and a day and returns the name of
# the day of the week as text, like "Saturday".
# Import the module and test the three functions.

print("\n--- Exercise 6 ---\n")

import date_tools

print(date_tools.calculate_age(2005, 11, 2))
print(date_tools.days_left(2055, 12, 24))
print(date_tools.get_weekday(2026, 11, 10))