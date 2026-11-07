# Exercise 5 Distance between points
# Write a function that receives two points, each one a tuple (x, y), and returns the distance
# between them, rounded to 2 decimals.
# Example: (0, 0) and (3, 4) are 5.0 apart.

print("--- Exercise 5 ---\n")

import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return round(result, 2)

print(distance((0, 0), (3, 4)))
print(distance((12, 5), (17, 8)))

# Exercise 6 Dice roller
# Write a function that receives a number of dice and returns a list with the result of rolling
# that many six-sided dice.

print("\n--- Exercise 6 ---\n")

import random

def dice(n):
    results = []
    for roll in range(n):
        results.append(random.randint(1, 6))
    return results

print(dice(2))
print(dice(4))

# Exercise 7 Days left
# Write a function that receives a year, a month and a day, and returns how many days are left
# until that date. If the date is today or has already passed, return 0.

print("\n--- Exercise 7 ---\n")

from datetime import datetime

def days_left(y, m, d):
    date = datetime(y, m, d)
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    
    total_days = (date - today).days

    if total_days < 0:
        return 0
    return total_days

now = datetime.now()

print(days_left(2038, 12, 24)) # Future
print(days_left(now.year, now.month, now.day)) # Today
print(days_left(2005, 6, 1))  # Already passed

# Exercise 8 Build a path
# Write a function that receives a folder name, a subfolder name and a file name, and returns
# the full path joined with the separator of the system.

print("\n--- Exercise 8 ---\n")

import os

def build_path(folder, subfolder, file):
    path = os.path.join(folder, subfolder, file)
    return path

path = build_path("fundamentals", "modules", "practice2.py")
print(path)
print(os.path.exists(path)) # True if exists False if not
print(os.path.basename(path)) # File name