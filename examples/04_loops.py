# ============================================================
# 04 - Loops in Python
# ============================================================
# Loops let you repeat a block of code multiple times.
# Python has two types: for loops and while loops.

# ============================================================
# FOR Loops
# ============================================================
# Use for loops when you know how many times to repeat.

# --- Loop over a range of numbers ---
for i in range(5):
    print(i)          # prints 0, 1, 2, 3, 4

print("---")

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)          # 1, 3, 5, 7, 9

print("---")

# Count down
for i in range(5, 0, -1):
    print(i)          # 5, 4, 3, 2, 1

print("---")

# --- Loop over a list ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("---")

# --- Loop over a string (character by character) ---
for letter in "Python":
    print(letter)

print("---")

# --- enumerate() → get index AND value ---
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")
# 0: red
# 1: green
# 2: blue

print("---")

# ============================================================
# WHILE Loops
# ============================================================
# Use while loops when you repeat UNTIL a condition is False.

count = 0
while count < 5:
    print(count)
    count += 1        # IMPORTANT: always update or you'll loop forever!

print("---")

# --- Classic: ask for input until valid ---
# while True:
#     answer = input("Type 'quit' to exit: ")
#     if answer == "quit":
#         break

# ============================================================
# Loop Control: break, continue, pass
# ============================================================

# break → exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)          # 0, 1, 2, 3, 4

print("---")

# continue → skip the rest of this iteration, keep looping
for i in range(10):
    if i % 2 == 0:
        continue      # skip even numbers
    print(i)          # 1, 3, 5, 7, 9

print("---")

# pass → do nothing (placeholder)
for i in range(3):
    pass              # no error, loop runs but does nothing

# ============================================================
# Nested Loops (a loop inside a loop)
# ============================================================
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()           # newline after each row
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)

print("---")

# ============================================================
# Practical Examples
# ============================================================

# Sum all numbers from 1 to 100
total = 0
for n in range(1, 101):
    total += n
print(f"Sum 1–100: {total}")    # 5050

# Find all even numbers in a list
numbers = [3, 7, 2, 8, 1, 4, 9, 6]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(f"Even numbers: {evens}")  # [2, 8, 4, 6]

# Multiplication table for 3
print("Multiplication table for 3:")
for i in range(1, 11):
    print(f"3 × {i} = {3 * i}")
