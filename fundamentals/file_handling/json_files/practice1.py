import json

folder = "fundamentals/file_handling/json_files/"

# Exercise 1 Save a dictionary
# Write a function that receives a file path and a dictionary, and saves the dictionary
# in that file as JSON, readable, with 4 spaces of indentation.

print("--- Exercise 1 ---\n")

def save(file_path, dictionary):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4)

profile = {
    "name": "Ana",
    "age": 21,
    "active": True,
    "skills": ["Python", "SQL"],
    "address": {"city": "Guadalajara", "zip": "44100"},
}

save(folder + "profiles.json", profile)

# Exercise 2 Load a file
# Write a function that receives a file path and returns the data stored in that JSON file.
# If the file does not exist, or its content is not valid JSON, return None.

print("\n--- Exercise 2 ---\n")

def load(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return data

with open(folder + "invalid.json", "w", encoding="utf-8") as file:
    file.write("{'id': 7}")   # single quotes are not valid JSON

print(load(folder + "profiles.json"))   # {'name': 'Ana', 'age': 21, 'active': True, 'skills': ['Python', 'SQL'], 'address': {'city': 'Guadalajara', 'zip': '44100'}}
print(load(folder + "invalid.json"))    # None
print(load(folder + "missing.json"))    # None