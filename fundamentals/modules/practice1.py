# Exercise 1 Circle area
# Write a function that receives the radius of a circle and returns its area, 
# rounded to 2 decimals.

print("--- Exercise 1 ---\n")

from math import pi

def area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return round(pi * radius ** 2, 2)

try:
    print(f"The area of the circle is: {area(40)}")
except ValueError as e:
    print(e)

try:
    print(f"The area of the circle is: {area(-71)}")
except ValueError as e:
    print(e)

# Exercise 2 Pages needed
# Write a function that receives a total number of items and the number of items that fit in one page,
# and returns how many pages are needed to show all of them.
# Example: 25 items with 10 per page need 3 pages.

print("\n--- Exercise 2 ---\n")

import math

def pages_needed(total_items, items_per_page):
    return math.ceil(total_items / items_per_page)

print(f"Total of pages nedeed: {pages_needed(50, 10)}")
print(f"Total of pages nedeed: {pages_needed(25, 7)}")

# Exercise 3 Random pick
# Write a function that receives a list and returns one random item of that list.
# If the list is empty, return None.

print("\n--- Exercise 3 ---\n")

import random

def random_pick(items):
    if not items:
        return None
    return random.choice(items)

products = ["Laptop", "Mouse", "Monitor"]
empty = []

print(f"Random item: {random_pick(products)}")
print(f"Random item: {random_pick(empty)}")

# Exercise 4 Today as text
# Write a function that receives no arguments and returns 
# today's date as text, in the format DD/MM/YYYY.

print("\n--- Exercise 4 ---\n")

from datetime import datetime

def today():
    return datetime.now().strftime("%d/%m/%Y")

print(today())