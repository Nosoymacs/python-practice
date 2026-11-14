import json

# The paths are relative to python/, the folder where the program is RUN.
folder = "fundamentals/file_handling/json_files/"

# 1. WHAT IS JSON
# JSON is a text format to store structured data. It is what most APIs send and receive.
# It maps almost directly to Python:
#
#   JSON object  {"a": 1}      <->  dict
#   JSON array   [1, 2, 3]     <->  list
#   JSON string  "text"        <->  str
#   JSON number  1 or 1.5      <->  int or float
#   JSON true / false          <->  True / False
#   JSON null                  <->  None

# json.load()   -> JSON file to Python dict/list
# json.loads()  -> JSON str to Python dict/list
# json.dump()   -> Python dict/list to JSON file
# json.dumps()  -> Python dict/list to JSON str

# 2. WRITING A FILE WITH json.dump
# indent=4 makes the file readable. Without it, everything goes on one line.
# Unlike CSV, you do not need newline="".

student = {
    "name": "Ana",
    "age": 21,
    "active": True,
    "grades": [9.5, 8.0, 10],
    "address": {"city": "Guadalajara", "zip": "44100"},
    "graduated": None,
}

with open(folder + "student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

# 3. READING A FILE WITH json.load
# It returns the Python object: here, a dictionary.

with open(folder + "student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(type(data))      # <class 'dict'>
print(data["name"])    # Ana

# 4. NESTED DATA
# Go level by level: keys for dictionaries, positions for lists.

print(data["address"]["city"])   # Guadalajara
print(data["grades"][0])         # 9.5

# 5. STRINGS INSTEAD OF FILES: dumps AND loads
# The "s" stands for string. They do the same, but without a file.

text = json.dumps({"id": 1, "tags": ["a", "b"]})
print(text)                       # {"id": 1, "tags": ["a", "b"]}
print(type(text))                 # <class 'str'>

back = json.loads(text)
print(back["tags"])               # ['a', 'b']

# 6. ACCENTS: ensure_ascii=False
# By default, special characters are written as codes.

print(json.dumps({"city": "México"}))                         # {"city": "M\u00e9xico"}
print(json.dumps({"city": "México"}, ensure_ascii=False))     # {"city": "México"}

# With a file, use it together with encoding="utf-8":
# json.dump(data, file, indent=4, ensure_ascii=False)

# 7. WHAT CHANGES WHEN YOU SAVE AND LOAD
# Not everything in Python exists in JSON.

original = {1: "one", "pair": (1, 2)}
copy = json.loads(json.dumps(original))
print(copy)    # {'1': 'one', 'pair': [1, 2]}
# - the number key 1 became the text "1": JSON keys are always text
# - the tuple became a list: JSON only has arrays

# 8. LIST OF DICTIONARIES: THE MOST COMMON SHAPE
# It looks like a CSV table: each dictionary is a row.

products = [
    {"name": "Laptop", "price": 15000, "stock": 4},
    {"name": "Mouse", "price": 250, "stock": 30},
]

with open(folder + "products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4)

# 9. MODIFYING A FILE: read, change, write back
# "w" erases the file, so first you read everything, change it in memory,
# and then write it all again.

with open(folder + "products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

products.append({"name": "Monitor", "price": 4800, "stock": 7})
products[0]["stock"] = 3

with open(folder + "products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4)

# 10. ERRORS
# FileNotFoundError: the file does not exist.
# json.JSONDecodeError: the text is not valid JSON. It is a kind of ValueError.
# TypeError: you tried to save something JSON does not know, like a datetime.

try:
    json.loads("{'name': 'Ana'}")       # single quotes are not valid JSON
except json.JSONDecodeError as e:
    print(e)    # Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

try:
    with open(folder + "missing.json", "r", encoding="utf-8") as file:
        json.load(file)
except FileNotFoundError:
    print("The file does not exist")

try:
    from datetime import datetime
    json.dumps({"now": datetime.now()})
except TypeError as e:
    print(e)    # Object of type datetime is not JSON serializable

# 11. THINGS TO AVOID
# - JSON needs double quotes: single quotes are not valid.
# - No trailing commas and no comments inside a JSON file.
# - Opening with "w" to "add" something: it erases the file. Read, change and write back.
# - Forgetting that loaded numbers keep their type, but keys are always text.