# Folder path
folder = "fundamentals/file_handling/txt_files/" 

# Helper to print the content of a file and check the results
def show_file(path):
    with open(path, "r", encoding="utf-8") as file:
        print(file.read())

# Exercise 9 Numbered copy
# Write a function that receives a source path and a destination path, and writes every line
# of the source into the destination with its line number at the start, like "1: First line".
# The numbering starts at 1.

print("--- Exercise 9 ---\n")

with open(folder + "fruits.txt", "w", encoding="utf-8") as file:
    file.write("Apple\nBanana\nCherry\n")

def numbered_copy(source, destination):
    with open(source, "r", encoding="utf-8") as source_file:
        with open(destination, "w", encoding="utf-8") as destination_file:
            i = 1
            for line in source_file:
                destination_file.write(f"{i}: {line}")
                i += 1

numbered_copy(folder + "fruits.txt", folder + "numbered_fruits.txt")
show_file(folder + "numbered_fruits.txt")

# Exercise 10 Merge files
# Write a function that receives a list of file paths and a destination path, and writes into
# the destination the content of all those files, one after another and in the same order.
# The files that do not exist are skipped. Return how many files were actually merged.

print("\n--- Exercise 10 ---\n")

with open(folder + "colors.txt", "w", encoding="utf-8") as file:
    file.write("Red\nGreen\nBlue\n")

with open(folder + "cities.txt", "w", encoding="utf-8") as file:
    file.write("Paris\nTokyo\n")

with open(folder + "blank.txt", "w", encoding="utf-8") as file:
    file.write("")

def merge_files(source_paths, destination):
    merged_files = 0

    with open(destination, "w", encoding="utf-8") as destination_file:
        for path in source_paths:
            try:
                with open(path, "r", encoding="utf-8") as source_file:
                    lines = source_file.readlines()
            except FileNotFoundError:
                continue

            destination_file.writelines(lines)
            merged_files += 1
            
    return merged_files

print(merge_files([folder + "colors.txt", folder + "cities.txt"], folder + "merged1.txt"))
show_file(folder + "merged1.txt")

print(merge_files([folder + "colors.txt", folder + "missing.txt", folder + "cities.txt"], folder + "merged2.txt"))
show_file(folder + "merged2.txt")

print(merge_files([folder + "blank.txt", folder + "colors.txt"], folder + "merged3.txt"))
show_file(folder + "merged3.txt")

# Exercise 11 Remove duplicates
# Write a function that receives a file path and removes the repeated lines of that file.
# Each line is kept only the first time it appears, and the original order is preserved.
# The file is rewritten with the result.

print("\n--- Exercise 11 ---\n")

with open(folder + "repeated_colors.txt", "w", encoding="utf-8") as file:
    file.write("Red\nBlue\nRed\nGreen\nBlue\nGreen\n")

def remove_duplicates(source):
    with open(source, "r", encoding="utf-8") as source_file:
        data = source_file.readlines()
        clean_data = []
        for line in data:
            if line not in clean_data:
                clean_data.append(line)
    with open(source, "w", encoding="utf-8") as rewritten_file:
        rewritten_file.writelines(clean_data)

remove_duplicates(folder + "repeated_colors.txt")
show_file(folder + "repeated_colors.txt")

# Exercise 12 Split in two
# Write a function that receives a source path and two destination paths, and writes the first half
# of the lines of the source into the first destination, and the rest into the second one.
# If the number of lines is odd, the first destination gets the extra line.

print("\n--- Exercise 12 ---\n")

with open(folder + "four_lines.txt", "w", encoding="utf-8") as file:
    file.write("Python\nPandas\nNumpy\nScikit-Learn\n")

with open(folder + "five_lines.txt", "w", encoding="utf-8") as file:
    file.write("Mouse\nKeyboard\nMonitor\nCPU\nGPU\n")

def split_in_two(source, destination1, destination2):
    with open(source, "r", encoding="utf-8") as source_file:
        lines = source_file.readlines()

    middle = len(lines) // 2
    if len(lines) % 2 != 0:
        middle += 1  

    with open(destination1, "w", encoding="utf-8") as first_file:
        first_file.writelines(lines[:middle])

    with open(destination2, "w", encoding="utf-8") as second_file:
        second_file.writelines(lines[middle:])

split_in_two(folder + "four_lines.txt", folder + "part_A.txt", folder + "part_B.txt")
split_in_two(folder + "five_lines.txt", folder + "part_X.txt", folder + "part_Y.txt")

for name in ["part_A.txt", "part_B.txt", "part_X.txt", "part_Y.txt"]:
    print(name)
    show_file(folder + name)