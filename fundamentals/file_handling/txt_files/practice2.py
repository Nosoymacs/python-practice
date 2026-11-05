folder = "fundamentals/file_handling/txt_files/"
with open(folder + "mixed.txt", "w", encoding="utf-8") as file:
    file.write("Max\n\nAna\n")

with open(folder + "empty.txt", "w", encoding="utf-8") as file:
    file.write("")

# Exercise 5 Clean lines
# Write a function that receives a file path and returns a list with the lines of the file,
# without the line break at the end of each one. Empty lines are skipped.
# If the file does not exist, return an empty list.

print("--- Exercise 5 ---\n")

def clean_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                data.append(line)
            return data
    except FileNotFoundError:
        return []

print(clean_lines(folder + "countries.txt"))
print(clean_lines(folder + "mixed.txt"))
print(clean_lines(folder + "missing.txt"))

# Exercise 6 Search lines
# Write a function that receives a file path and a text, and returns a list with the lines
# of the file that contain that text, ignoring uppercase and lowercase.
# If the file does not exist, return an empty list.

print("\n--- Exercise 6 ---\n")

def search_lines(path, text):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = []
            text = text.lower()
            for line in file:
                if text in line.lower():
                    data.append(line.strip())
            return data
    except FileNotFoundError:
        return []

print(search_lines(folder + "countries.txt", "Mexico"))
print(search_lines(folder + "countries.txt", "n"))
print(search_lines(folder + "countries.txt", "Taco Bell"))

# Exercise 7 Copy a file
# Write a function that receives a source path and a destination path, and copies the content
# of the source file into the destination file.
# Return True if the copy worked, and False if the source file does not exist.

print("\n--- Exercise 7 ---\n")

def copy_file(source, destination):
    try:
        with open(source, "r", encoding="utf-8") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        return False
    with open(destination, "w", encoding="utf-8") as destination_file:
        destination_file.write(content)
    return True

print(copy_file(folder+"countries.txt", folder+"countries_copy.txt"))
print(copy_file(folder+"missing.txt", folder+"countries_copy.txt"))

# Exercise 8 Longest line
# Write a function that receives a file path and returns the longest line of the file,
# without the line break at the end.
# If the file does not exist or is empty, return None.

print("\n--- Exercise 8 ---\n")

def longest_line(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            longest = None
            for line in file:
                line = line.strip()
                if longest is None or len(line) > len(longest):
                    longest = line
            return longest
    except FileNotFoundError:
        return None

print(longest_line(folder + "countries.txt"))
print(longest_line(folder + "missing.txt"))
print(longest_line(folder + "empty.txt"))