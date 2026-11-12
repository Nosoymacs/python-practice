import csv

# The paths are relative to python/, the folder where the program is RUN.
folder = "fundamentals/file_handling/csv_files/"

# WHAT IS A CSV FILE
# A CSV (comma-separated values) is a text file that stores a table:
# one row per line, and the values of each row separated by commas.
# The first row usually holds the column names.

# You could read it like any txt file, but values can contain commas or quotes
# (for example "Monitor, 27 inch"), and cutting the text by hand breaks.
# The csv module handles all of that.

# 1. WRITING ROWS WITH csv.writer
# newline="" is required when you open a CSV file for writing.
# Without it, Windows adds a blank line after every row.

print("--- 1 ---\n")

with open(folder + "products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "price", "stock"])    # one row: a list of values
    writer.writerows([                             # several rows at once: a list of lists
        ["Laptop", 15000, 4],
        ["Mouse", 250, 30],
        ["Monitor, 27 inch", 4800, 7],             # this name has a comma: csv adds the quotes
    ])

# 2. READING ROWS WITH csv.reader
# Every row is a list of strings, even the numbers.

print("\n--- 2 ---\n")

with open(folder + "products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 3. SKIPPING THE HEADER AND CONVERTING VALUES
# next(reader) takes the next row and moves forward, so the loop starts after the header.
# The numbers arrive as text: convert them with int() or float() before calculating.

print("\n--- 3 ---\n")

with open(folder + "products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    total = 0
    for row in reader:
        total += float(row[1]) * int(row[2])    # price * stock

print(header)
print(total)    # 101100.0

# 4. WRITING WITH DICTIONARIES: csv.DictWriter
# Each row is a dictionary, and the keys must match the column names.

print("\n--- 4 ---\n")

fields = ["name", "price", "stock"]

with open(folder + "products2.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()   # writes the column names
    writer.writerow({"name": "Keyboard", "price": 900, "stock": 12})
    writer.writerows([{"name": "Webcam", "price": 1100, "stock": 0},
                     {"name": "Mouse", "price": 800, "stock": 53},
                     {"name": "Monitor", "price": 2100, "stock": 9}])

# 5. READING WITH DICTIONARIES: csv.DictReader
# It uses the first row as the keys, so you do not skip the header yourself
# and you read by column name instead of by position.

print("\n--- 5 ---\n")

with open(folder + "products2.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], int(row["stock"]))    # values are still text: convert them

# 6. APPENDING ROWS
# "a" adds rows at the end. Do not write the header again.

print("\n--- 6 ---\n")

with open(folder + "products2.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writerow({"name": "Headphones", "price": 700, "stock": 8})

# 7. OTHER SEPARATORS
# Excel in Spanish-speaking regions often saves CSV files with ";" instead of ",".
# Tell the reader or the writer which separator to use with delimiter.

print("\n--- 7 ---\n")

with open(folder + "semicolon.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["name", "price"])
    writer.writerow(["Laptop", "15000.50"])

with open(folder + "semicolon.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)    # ['name', 'price'] and ['Laptop', '15000.50']

# 8. MISSING FILES
# Opening a missing CSV raises FileNotFoundError, exactly like a txt file.

print("\n--- 8 ---\n")

try:
    with open(folder + "missing.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        print(list(reader))
except FileNotFoundError:
    print("The file does not exist")

# 9. THINGS TO AVOID
# - Forgetting newline="" when you open the file: blank lines appear between rows on Windows.
# - Doing math with the values you read without converting them: "250" * 2 gives "250250".
# - Writing the header twice when you append rows.
# - If Excel shows broken accents when it opens a file you wrote, use encoding="utf-8-sig".