import json
import csv

folder = "fundamentals/file_handling/json_files/"

# Exercise 5 CSV to JSON
# Write a function that receives the path of a CSV file with a header and the path of a JSON file,
# and writes the rows of the CSV as a list of dictionaries in the JSON file.
# The values that are whole numbers must be saved as numbers, not as text.
# Return how many rows were written. If the CSV file does not exist, return None.

print("--- Exercise 5 ---\n")

def csv_to_json(csv_path, json_path):
    count = 0

    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = []

            for row in reader:
                for key, value in row.items():
                    try:
                        row[key] = int(row[key])
                    except ValueError:
                        continue
                data.append(row)
                count += 1

    except FileNotFoundError:
        return None

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return count

with open(folder + "inventory.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows([
        ["sku", "name", "stock", "price"],
        ["A100", "Laptop", 4, 15000.50],
        ["B200", "Mouse", 30, 250],
        ["C300", "Monitor, 27 inch", 7, 4800],
    ])

print(csv_to_json(folder + "inventory.csv", folder + "inventory.json"))
print(csv_to_json(folder + "missing.csv", folder + "inventory.json"))

# Exercise 6 Grade averages
# Write a function that receives the path of a JSON file that contains a list of students,
# each one a dictionary with a "name" and a list of "grades", and returns a dictionary
# with the name of each student and the average of their grades, rounded to 1 decimal.
# A student with no grades has an average of 0.

print("\n--- Exercise 6 ---\n")

def grade_averages(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    averages = {}

    for student in data:
        try:
            averages[student["name"]] = round(sum(student["grades"]) / len(student["grades"]), 1)
        except ZeroDivisionError:
            averages[student["name"]] = 0

    return averages

students = [
    {"name": "Ana", "grades": [9, 8, 10]},
    {"name": "Luis", "grades": [7, 6]},
    {"name": "Marta", "grades": []},
]

with open(folder + "students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print(grade_averages(folder + "students.json"))