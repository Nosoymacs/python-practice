folder = "fundamentals/file_handling/txt_files/"

# Exercise 1 Write lines
# Write a function that receives a file path and a list of texts, and writes each text on its own line
# in that file, replacing any previous content.
# Example: ["Max", "Ana"] should leave a file with two lines.

print("--- Exercise 1 ---\n")

def write_lines(path, data: list):
    with open(path, "w", encoding="utf-8") as file:
        for text in data:
            file.write(text + "\n")

countries = ["Canada", "USA", "Mexico"]
write_lines(folder+"countries.txt", countries)

# Exercise 2 Read everything
# Write a function that receives a file path and returns the whole content of the file as one string.
# If the file does not exist, return None.

print("\n--- Exercise 2 ---\n")

def read_all(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None

print(read_all(folder + "countries.txt"))
print(read_all(folder + "missing.txt"))

# Exercise 3 Add a line
# Write a function that receives a file path and a text, and adds the text as a new line
# at the end of the file, keeping the content that was already there.

print("\n--- Exercise 3 ---\n")

def write_newline(path, text: str):
    with open(path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

write_newline(folder+"countries.txt", "Brazil")
write_newline(folder+"countries.txt", "Argentina")
print(read_all(folder + "countries.txt"))

# Exercise 4 Count lines
# Write a function that receives a file path and returns how many lines the file has.
# If the file does not exist, return None.

print("\n--- Exercise 4 ---\n")

def count_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return None

print(count_lines(folder + "countries.txt"))
print(count_lines(folder + "missing.txt"))