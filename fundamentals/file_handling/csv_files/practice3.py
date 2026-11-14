import csv

folder = "fundamentals/file_handling/csv_files/"
fields = ["make", "model", "year", "color"]

with open(folder + "cars.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields, delimiter=";")
    writer.writeheader()
    writer.writerows([{"make": "Honda", "model": "Civic", "year": 2024, "color": "Gray"},
                     {"make": "Toyota", "model": "Corolla", "year": 2002, "color": "Blue"},
                     {"make": "Nissan", "model": "Sentra", "year": 2020, "color": "Black"}])

# Exercise 7 Change the separator
# Write a function that receives a source path, whose values are separated by ";", and a destination path,
# and writes the same data into the destination separated by ",".
# Return how many rows were copied, header included.

print("--- Exercise 7 ---\n")

def change_separator(source_path, destination_path):
    count = 0

    with open(source_path, "r", newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file, delimiter=";")

        with open(destination_path, "w", newline="", encoding="utf-8") as destination_file:
            writer = csv.DictWriter(destination_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            count += 1

            for row in reader:
                writer.writerow(row)
                count += 1

    return count

print(change_separator(folder + "cars.csv", folder + "copy_cars.csv"))

# Exercise 8 Totals by group
# Write a function that receives a file path, the name of a column to group by and the name of a numeric column,
# and returns a dictionary with the total of the numeric column for each different value of the group column.
# Example: the total sold by each seller.

print("\n--- Exercise 8 ---\n")

with open(folder + "sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows([
        ["seller", "product", "amount"],
        ["Ana", "Laptop", 15000],
        ["Luis", "Mouse", 250],
        ["Ana", "Monitor, 27 inch", 4800],   
        ["Marta", "Keyboard", 900],
        ["Luis", "Webcam", 1100],
        ["Ana", "Headphones", 700],
    ])

def total_by_group(file_path, group_column, numeric_column):
    data = {}

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row[group_column] not in data:
                data[row[group_column]] = float(row[numeric_column])
            else:
                data[row[group_column]] += float(row[numeric_column])
    
    return data

print(total_by_group(folder + "sales.csv", "seller", "amount"))
print(total_by_group(folder + "sales.csv", "product", "amount"))

# Exercise 9 Remove incomplete rows
# Write a function that receives a source path and a destination path, and writes into the destination
# only the rows of the source that have no empty value in any column, keeping the header.
# Return how many rows were discarded.

print("\n--- Exercise 9 ---\n")

incomplete_fields = ["id", "name", "city"]

with open(folder + "contacts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=incomplete_fields)
    writer.writeheader()
    writer.writerows([
        {"id": "1", "name": "Ana", "city": "Guadalajara"},       
        {"id": "", "name": "Luis", "city": "Monterrey"},         
        {"id": "3", "name": "Marta", "city": ""},                   
        {"id": "4", "name": "Oscar", "city": "Cancun"},             
        {"id": "5", "name": "", "city": "Puebla"},                
        {"id": "6", "name": "Sofia, Maria", "city": "Merida"},       
    ])

def remove(source_path, destination_path):
    count = 0

    with open(source_path, "r", newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)

        with open(destination_path, "w", newline="", encoding="utf-8") as destination_file:
            writer = csv.DictWriter(destination_file, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                complete = True

                for key, value in row.items():
                    if not value.strip():
                        complete = False

                if not complete:
                    count += 1
                    continue

                writer.writerow(row)

    return count

print(remove(folder + "contacts.csv", folder + "valid_contacts.csv"))