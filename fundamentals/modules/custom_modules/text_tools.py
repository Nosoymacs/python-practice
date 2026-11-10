# Module text_tools.py
# A module is a normal .py file. Other files can import its functions and variables.

VOWELS = "aeiou"

def count_vowels(text):
    total = 0
    for letter in text.lower():
        if letter in VOWELS:
            total += 1
    return total

def shout(text):
    return text.upper() + "!"

print(f"text_tools is running with __name__ = {__name__}")

if __name__ == "__main__":
    # This block only runs when you run THIS file directly, never when it is imported
    print(count_vowels("Hello World"))
    print(shout("hello"))               