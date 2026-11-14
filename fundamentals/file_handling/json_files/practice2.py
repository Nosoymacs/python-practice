import json
import os

folder = "fundamentals/file_handling/json_files/"

# Reset the files that must NOT exist before the tests, so I can run the code several times
for name in ["not_exists.json", "missing.json"]:
    if os.path.exists(folder + name):
        os.remove(folder + name)

# Helper to print the content of a JSON file and check the results
def show_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        print(json.load(file))

# Exercise 3 Update a value
# Write a function that receives a file path that contains a JSON object, a key and a value,
# and sets that key to that value in the file, keeping the rest of the data.
# If the file does not exist, create it with an object that has only that key.

print("--- Exercise 3 ---\n")

def update(file_path, key, value):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

    data[key] = value

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

settings = {
    "app": "MyApp",
    "version": "1.0",
    "debug": False,
    "limits": {"users": 10, "files": 5},
}

with open(folder + "settings.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)

update(folder + "settings.json", "version", 2.0)
update(folder + "not_exists.json", "app", "NewApp")

show_json(folder + "settings.json")      # same data, with "version" set to 2.0
show_json(folder + "not_exists.json")    # {'app': 'NewApp'}

# Exercise 4 Add to a list
# Write a function that receives a file path that contains a JSON list and an item,
# and adds the item at the end of the list in the file, keeping the rest of the items.
# If the file does not exist, create it with a list that has only that item.

print("\n--- Exercise 4 ---\n")

def add(file_path, item):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(item)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

tasks = [
    {"id": 1, "title": "Study JSON", "done": True},
    {"id": 2, "title": "Install venv", "done": False},
]

with open(folder + "tasks.json", "w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)

task = {"id": 3, "title": "Update python", "done": False}

add(folder + "tasks.json", task)
add(folder + "missing.json", task)

show_json(folder + "tasks.json")         # three tasks
show_json(folder + "missing.json")       # a list with only the new task