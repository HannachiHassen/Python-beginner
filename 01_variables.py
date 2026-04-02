# ============================================================
# 01 - Variables in Python
# ============================================================
# A variable is a named container that stores a value.
# Python figures out the type automatically (dynamic typing).

# --- Strings ---
name = "Alice"
greeting = 'Hello, World!'

# --- Numbers ---
age = 25          # int (whole number)
height = 5.7      # float (decimal number)

# --- Booleans ---
is_student = True
has_pet = False

# --- None (represents "nothing" / no value) ---
middle_name = None

# --- Printing variables ---
print(name)          # Alice
print(age)           # 25
print(is_student)    # True

# --- Checking the type of a variable ---
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>

# --- Updating a variable ---
age = 26             # just reassign it
print(age)           # 26

# --- Multiple assignment (assign several at once) ---
x, y, z = 1, 2, 3
print(x, y, z)       # 1 2 3

# --- Swap two variables (Python makes this easy!) ---
a, b = 10, 20
a, b = b, a
print(a, b)          # 20 10

# --- Naming rules ---
# ✅ Good names
user_name = "Bob"
total_score = 100
_private = "hidden"

# ❌ Bad names (would cause errors)
# 2fast = True        # can't start with a number
# my-var = 5          # hyphens not allowed
# class = "Math"      # 'class' is a reserved keyword
