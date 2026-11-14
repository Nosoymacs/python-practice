import csv
import os

folder = "fundamentals/file_handling/csv_files/"
fields = ["id", "name", "salary"]

with open(folder + "employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows([{"id": "1", "name": "Max Gonzalez", "salary": 22000},
                     {"id": "2", "name": "Mildred Renteria", "salary": 18000},
                     {"id": "3", "name": "Oswaldo Galvan", "salary": 19500}])
    
# Exercise 4 Column total
# Write a function that receives a file path and the name of a numeric column,
# and returns the sum of all the values of that column.
# If the file or the column does not exist, return None.

print("--- Exercise 4 ---\n")

def column_total(file_path, column_name):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            total = 0

            for row in reader:
                total += float(row[column_name])

            return total

    except (FileNotFoundError, KeyError):
        return None

print(column_total(folder + "employees.csv", "salary"))
print(column_total(folder + "missing.csv", "salary"))
print(column_total(folder + "employees.csv", "missing"))

# Exercise 5 Filter rows
# Write a function that receives a file path, a column name and a value, and returns a list with the rows
# whose value in that column is equal to the given one, each row as a dictionary.
# If the file does not exist, return an empty list.

print("\n--- Exercise 5 ---\n")

def filter_rows(file_path, column_name, value):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = []

            for row in reader:
                if row[column_name] == value:
                    data.append(row)

            return data
        
    except FileNotFoundError:
        return []

print(filter_rows(folder + "employees.csv", "id", "1"))
print(filter_rows(folder + "employees.csv", "id", "99"))
print(filter_rows(folder + "missing.csv", "id", "1"))

# Exercise 6 Add a record
# Write a function that receives a file path and a dictionary, and adds the dictionary as a new row
# at the end of the CSV file, without writing the header again.
# If the file does not exist or is empty, create it first, with a header made from the keys of the dictionary.

print("\n--- Exercise 6 ---\n")

def add_record(file_path, dictionary):
    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=dictionary.keys())

        if os.path.getsize(file_path) == 0: # Returns the file size in bytes
            writer.writeheader()

        writer.writerow(dictionary)

data = {"id": "4", "name":"Alavaro Carreras", "salary": 43000}
add_record(folder + "employees.csv", data)
add_record(folder + "not_exist.csv", data)
add_record(folder + "empty.csv", data)