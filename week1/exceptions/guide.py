# ==========================================
# PART 3: Exceptions
# ==========================================

# 1. WHAT IS AN EXCEPTION
# An exception is an error that happens while the program is running.
# If it is not handled, the program stops and Python shows a traceback.
# Read the traceback from the bottom: the last line says the error type and why.

# print(10 / 0)  # ZeroDivisionError: division by zero (uncomment to see it)

# 2. TRY / EXCEPT
# Code that might fail goes in 'try'. If an error happens, Python jumps to 'except'.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

# 3. COMMON EXCEPTION TYPES
# ZeroDivisionError: dividing by zero
# ValueError:        right type, wrong value, e.g. int("abc")
# TypeError:         wrong type, e.g. "5" + 5
# KeyError:          a dictionary key does not exist
# IndexError:        a list index is out of range
# FileNotFoundError: the file does not exist

try:
    number = int("abc")
except ValueError:
    print("That is not a valid number")

# 4. CATCHING THE ERROR OBJECT WITH 'as'
# 'as e' gives you the exception so you can read its message.

try:
    data = {"name": "Max"}
    print(data["age"])
except KeyError as e:
    print(f"Missing key: {e}")

# 5. MULTIPLE EXCEPT BLOCKS
# Python checks them in order and runs only the first one that matches.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Cannot divide by zero
print(safe_divide(10, "a"))   # Both values must be numbers

# You can also catch several types in a single block:
try:
    int("abc")
except (ValueError, TypeError):
    print("Invalid input")

# 6. ELSE AND FINALLY
# else:    runs only if the 'try' block had NO error.
# finally: runs ALWAYS, whether there was an error or not.
#          It is used for cleanup, such as closing a file.

try:
    number = int("42")
except ValueError:
    print("Not a number")
else:
    print(f"Converted: {number}")
finally:
    print("This always runs")

# 7. RAISE: CREATE YOUR OWN ERROR
# Use 'raise' to stop a function when it receives an invalid value.

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)  # Age cannot be negative

# 8. WHAT NOT TO DO
# A bare 'except:' catches EVERYTHING, even errors you did not expect,
# and hides real bugs. Always name the exception type.

# Bad:
# try:
#     risky()
# except:
#     pass

# Good:
# try:
#     risky()
# except ValueError:
#     print("Invalid value")