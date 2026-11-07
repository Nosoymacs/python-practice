# Exercise 9 Password generator
# Write a function that receives a length and returns a random password of that length,
# made of lowercase letters and digits.

print("--- Exercise 9 ---\n")

import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password = generate_password(12)
print(f"Password: {password}")

# Exercise 10 Shuffled copy
# Write a function that receives a list and returns a new list with the same items in random order.
# The original list must stay unchanged.

print("\n--- Exercise 10 ---\n")

import random

def shuffled_copy(items):
    shuffled_items = random.sample(items, len(items))
    return shuffled_items

numbers = [1, 2, 3, 4, 5]
numbers_copy = shuffled_copy(numbers)

print(f"Original: {numbers}")
print(f"Shuffled copy: {numbers_copy}")

# Exercise 11 Age in years
# Write a function that receives a birth year, month and day, and returns the age in full years
# as of today. A person who has not had their birthday yet this year is one year younger.

print("\n--- Exercise 11 ---\n")

from datetime import datetime

def calculate_age(y, m, d):
    birth = datetime(y, m, d)
    now = datetime.now()

    age = now.year - birth.year

    if (now.month, now.day) < (birth.month, birth.day):
        age -= 1

    return age

print(calculate_age(2005, 11, 2))   
print(calculate_age(2001, 9, 11))   
print(calculate_age(2000, 12, 25))  

# Exercise 12 Log entry
# Write a function that receives a message and a file path, and adds a line at the end of that file
# with the current date and time followed by the message, like "2026-11-06 22:23:47 - Message".
# If the folder of the path does not exist, do not write anything and return False.
# Otherwise, return True.

print("\n--- Exercise 12 ---\n")

import os
from datetime import datetime

def log_entry(message, path):
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        return False

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{now} - {message}\n")

    return True

txt_path = os.path.join("fundamentals", "modules", "notes.txt")

with open(txt_path, "w", encoding="utf-8") as file:
    file.write("")

missing_path = os.path.join("missing_folder", "missing_subfolder", "missing.txt")

print(log_entry("Minecraft is cool", txt_path))
print(log_entry("Hello World", txt_path))
print(log_entry("Missing text", missing_path))

with open(txt_path, "r", encoding="utf-8") as file:
    print(file.read())

print(os.path.exists("missing_folder"))  