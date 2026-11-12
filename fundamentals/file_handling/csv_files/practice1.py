folder = "fundamentals/file_handling/csv_files/"

import csv

# Exercise 1 Write rows
# Write a function that receives a file path and a list of rows, each row a list of values,
# and writes them into a CSV file, replacing any previous content.
# The first row of the list is the header.

print("--- Exercise 1 ---\n")

def write_rows(file_path, data):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

info = [["name", "age", "career"],
        ["Max", 21, "IT"],
        ["Mildred", 18, "Marketing"],
        ["John", 25, "Medicine"]]

write_rows(folder + "students.csv", info)

# Exercise 2 Read rows
# Write a function that receives a file path and returns a list with all the data rows of the CSV file,
# each row as a list, without the header.
# If the file does not exist, return an empty list.

print("\n--- Exercise 2 ---\n")

def read_rows(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            data = []

            for row in reader:
                data.append(row)

            return data
        
    except FileNotFoundError:
        return []

print(read_rows(folder + "students.csv"))
print(read_rows(folder + "missing.csv"))

# Exercise 3 Count rows
# Write a function that receives a file path and returns how many data rows the CSV file has,
# without counting the header.
# If the file does not exist, return None.

print("\n--- Exercise 3 ---\n")

def count_rows(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            total = 0

            for row in reader:
                total += 1

            return total
        
    except FileNotFoundError:
        return None

print(count_rows(folder + "students.csv"))
print(count_rows(folder + "missing.csv"))