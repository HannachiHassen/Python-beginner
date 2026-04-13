# ============================================================
# 09 - Error Handling in Python
# ============================================================
# Errors (exceptions) happen. Good code handles them gracefully
# instead of crashing.

# ============================================================
# Common Errors You'll Encounter
# ============================================================
# TypeError    → wrong type  (e.g., "hello" + 5)
# ValueError   → right type, wrong value (e.g., int("abc"))
# ZeroDivisionError → dividing by zero
# IndexError   → list index out of range
# KeyError     → dictionary key not found
# FileNotFoundError → file doesn't exist

# ============================================================
# try / except Block
# ============================================================
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero.")

print("Program continues...")   # this still runs!

# ============================================================
# Catching Multiple Exceptions
# ============================================================
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both values must be numbers.")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error message, returns None
print(safe_divide(10, "x"))  # Error message, returns None

# ============================================================
# else and finally
# ============================================================
# else  → runs if NO exception occurred
# finally → ALWAYS runs (cleanup code)

def read_number(text):
    try:
        number = int(text)
    except ValueError:
        print(f"'{text}' is not a valid number.")
    else:
        print(f"Successfully converted: {number}")
    finally:
        print("Conversion attempt done.\n")

read_number("42")
read_number("hello")

# ============================================================
# Catching Any Exception (use sparingly!)
# ============================================================
try:
    x = int("bad input")
except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"Error type: {type(e).__name__}")

# ============================================================
# Raising Your Own Exceptions
# ============================================================
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is not realistic.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"Wrong type: {e}")

# ============================================================
# Practical Example: Safe User Input
# ============================================================
def get_positive_number(prompt="Enter a positive number: "):
    """Keep asking until user enters a valid positive number."""
    while True:
        try:
            # Simulating user input for this demo:
            user_input = "42"   # replace with input(prompt) in real use
            number = float(user_input)
            if number <= 0:
                raise ValueError("Number must be positive.")
            return number
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            break   # in real use, remove this break to keep looping

result = get_positive_number()
print(f"You entered: {result}")
