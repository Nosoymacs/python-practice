# TXT Files Guide


# The paths are relative to python/, the folder where the program is RUN.
folder = "fundamentals/file_handling/txt_files/"

# 1. OPENING A FILE
# open(name, mode) returns a file object. The most common modes are:
# "r": read (default). The file must exist.
# "w": write. Creates the file, or ERASES it if it already exists.
# "a": append. Creates the file, or adds to the end if it already exists.

# 2. WITH: THE SAFE WAY TO OPEN
# 'with' closes the file automatically when the block ends,
# even if an error happens inside it.

with open(f"{folder}notes.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")

# write() does not add a line break. You have to add "\n" yourself.

# 3. READING THE WHOLE FILE
# read() returns the entire content as one string.

with open(f"{folder}notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# 4. READING LINE BY LINE
# A file object can be used directly in a for loop.
# Each line includes the "\n" at the end, so strip() removes it.

with open(f"{folder}notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# 5. READLINES: ALL LINES IN A LIST
# readlines() returns a list with one string per line.

with open(f"{folder}notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)        # ['First line\n', 'Second line\n']
print(len(lines))   # 2

# 6. APPENDING
# "a" adds to the end without erasing what was already there.

with open(f"{folder}notes.txt", "a", encoding="utf-8") as file:
    file.write("Third line\n")

# 7. WRITING SEVERAL LINES AT ONCE
# writelines() writes a list of strings. It does not add "\n" either.

names = ["Max\n", "Mildred\n", "John\n"]

with open(f"{folder}names.txt", "w", encoding="utf-8") as file:
    file.writelines(names)

# 8. FILE NOT FOUND
# Opening a missing file in "r" mode raises FileNotFoundError.

try:
    with open(f"{folder}missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist")

# 9. WHY encoding="utf-8"
# It makes accents and special characters (á, é, ñ) save and read correctly,
# no matter which system runs the code. Windows may use a different default.

# 10. WHERE THE FILE IS CREATED
# A relative path is resolved from the folder where the program is RUN,
# not from where the .py file lives. Here the task runs from python/,
# so the path must start at fundamentals/. If the folder does not exist,
# open() with "w" raises FileNotFoundError: it creates files, not folders.