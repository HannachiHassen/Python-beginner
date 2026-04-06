# ============================================================
# 05 - Conditionals (if / elif / else)
# ============================================================
# Conditionals let your program make decisions.

# ============================================================
# Basic if / elif / else
# ============================================================
age = 18

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

# ============================================================
# Comparison Operators
# ============================================================
x = 10
print(x == 10)   # True  → equal to
print(x != 5)    # True  → not equal to
print(x > 5)     # True  → greater than
print(x < 5)     # False → less than
print(x >= 10)   # True  → greater than or equal
print(x <= 10)   # True  → less than or equal

# ============================================================
# Logical Operators: and, or, not
# ============================================================
temp = 22
is_raining = False

if temp > 20 and not is_raining:
    print("Great weather for a walk!")

score = 85
if score >= 90 or score == 85:
    print("You did well!")    # prints (second condition is True)

# ============================================================
# Checking Membership with 'in'
# ============================================================
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list!")

word = "Python"
if "Py" in word:
    print("The word starts with Py!")

# ============================================================
# Truthy and Falsy Values
# ============================================================
# These values are considered False in Python:
# False, 0, 0.0, "", [], {}, None

if "":
    print("this won't print")
else:
    print("empty string is falsy!")  # prints

if [1, 2, 3]:
    print("non-empty list is truthy!")  # prints

# ============================================================
# One-line (Ternary) Conditional
# ============================================================
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# ============================================================
# Nested Conditionals
# ============================================================
username = "admin"
password = "secret123"

if username == "admin":
    if password == "secret123":
        print("Welcome, admin!")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")

# ============================================================
# match / case (Python 3.10+, like switch in other languages)
# ============================================================
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Back to work.")
    case _:
        print("A regular weekday.")   # _ is the default
