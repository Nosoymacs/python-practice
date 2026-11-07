# Python Modules Guide

# 1. WHAT IS A MODULE
# A module is a .py file with code you can reuse: functions, variables, classes.
# Python comes with many ready-made modules (the "standard library").
# To use one, you import it first. By convention, imports go at the top of the file.

# 2. IMPORT A WHOLE MODULE
# After 'import math', you reach its content with module_name.item

import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.ceil(4.2))   # 5   (rounds up)
print(math.floor(4.8))  # 4   (rounds down)

# 3. IMPORT ONLY WHAT YOU NEED
# 'from module import name' lets you use the name directly, without the prefix.

from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)

# 4. ALIASES WITH 'as'
# 'as' gives the module a shorter name.
# for example "import pandas as pd".

import math as m

print(m.sqrt(9))  # 3.0

# 5. EXPLORING A MODULE
# help() shows the documentation of something, and dir() lists everything a module has.

help(math.sqrt)
print(dir(math))

# 6. RANDOM: RANDOM VALUES
# The results change every time you run the file.

import random

colors = ["Red", "Green", "Blue"]

print(random.randint(1, 10))  # a random integer from 1 to 10, both included
print(random.choice(colors))  # one random item of the list
random.shuffle(colors)        # shuffles the list IN PLACE and returns None
print(colors)

# A seed makes the results repeatable: the same seed gives the same numbers.
random.seed(42)
print(random.randint(1, 100))

# 7. DATETIME: DATES AND TIMES

from datetime import datetime, timedelta

now = datetime.now()
print(now)                              # current date and time
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d"))         # a date as text, e.g. 2026-11-06
print(now.strftime("%d/%m/%Y %H:%M"))   # another format, e.g. 06/11/2026 22:05

tomorrow = now + timedelta(days=1)      # timedelta is an amount of time
print(tomorrow.strftime("%Y-%m-%d"))

new_year = datetime(2027, 1, 1)         # a specific date
print((new_year - now).days)            # days left until that date

# 8. OS.PATH: BUILDING AND CHECKING PATHS
# os.path.join builds a path with the right separator for the system,
# so you do not have to glue strings with + "/".

import os

path = os.path.join("fundamentals", "file_handling", "txt_files", "notes.txt")

print(path)                    # on Windows it uses backslashes
print(os.path.exists(path))    # True if the file exists, False if not
print(os.path.basename(path))  # notes.txt
print(os.path.dirname(path))   # the folder part of the path

# 9. THINGS TO AVOID
# - 'from math import *' imports everything and you lose track of where names come from.
# - Never name your own file math.py or random.py. Python would import YOUR file
#   instead of the standard module, and 'import random' would stop working.