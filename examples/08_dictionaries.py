# ============================================================
# 08 - Dictionaries in Python
# ============================================================
# A dictionary stores data as key: value pairs.
# Like a real dictionary: you look up a word (key) to get its meaning (value).

# ============================================================
# Creating a Dictionary
# ============================================================
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

empty = {}
also_empty = dict()

# ============================================================
# Accessing Values
# ============================================================
print(person["name"])           # Alice
print(person.get("age"))        # 30
print(person.get("country"))    # None (no error if key missing)
print(person.get("country", "Unknown"))  # Unknown (default value)

# ============================================================
# Adding and Updating Items
# ============================================================
person["email"] = "alice@email.com"   # add new key
person["age"] = 31                    # update existing key
print(person)

# ============================================================
# Removing Items
# ============================================================
removed = person.pop("email")         # remove and return value
print(removed)                        # alice@email.com

del person["city"]                    # delete a key
print(person)

# ============================================================
# Checking Keys
# ============================================================
print("name" in person)        # True
print("country" in person)     # False

# ============================================================
# Looping Over a Dictionary
# ============================================================
student = {"name": "Bob", "grade": "A", "score": 95}

# Keys only
for key in student:
    print(key)

# Values only
for value in student.values():
    print(value)

# Keys and values together
for key, value in student.items():
    print(f"{key} → {value}")

# ============================================================
# Useful Dictionary Methods
# ============================================================
inventory = {"apple": 5, "banana": 12, "cherry": 3}

print(inventory.keys())     # dict_keys(['apple', 'banana', 'cherry'])
print(inventory.values())   # dict_values([5, 12, 3])
print(len(inventory))       # 3

inventory.update({"mango": 8, "apple": 10})  # add/update multiple
print(inventory)

copy = inventory.copy()     # make a shallow copy

# ============================================================
# Nested Dictionaries
# ============================================================
users = {
    "alice": {"age": 30, "role": "admin"},
    "bob":   {"age": 25, "role": "user"},
}

print(users["alice"]["role"])   # admin
print(users["bob"]["age"])      # 25

for username, info in users.items():
    print(f"{username} is a {info['role']}, age {info['age']}")

# ============================================================
# Dictionary Comprehension
# ============================================================
squares = {n: n**2 for n in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

words = ["apple", "banana", "kiwi"]
lengths = {word: len(word) for word in words}
print(lengths)   # {'apple': 5, 'banana': 6, 'kiwi': 4}
