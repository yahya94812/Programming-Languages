# Complete Python Tutorial: From Basics to Advanced

## Table of Contents
1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Data Types](#data-types)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Data Structures](#data-structures)
8. [String Manipulation](#string-manipulation)
9. [Object-Oriented Programming](#object-oriented-programming)
10. [File Handling](#file-handling)
11. [Error Handling](#error-handling)
12. [Modules and Packages](#modules-and-packages)
13. [List Comprehensions](#list-comprehensions)
14. [Lambda Functions](#lambda-functions)
15. [Decorators](#decorators)
16. [Generators](#generators)
17. [Context Managers](#context-managers)
18. [Working with JSON](#working-with-json)
19. [Important Built-in Functions](#important-built-in-functions)
20. [Best Practices](#best-practices)

---

## Getting Started

### Installation
Download Python from [python.org](https://python.org). Python 3.x is recommended.

### Running Python
```python
# Interactive mode
python3

# Run a script
python3 script.py
```

### Your First Program
```python
print("Hello, World!")
```

---

## Basic Syntax

### Comments
```python
# Single-line comment

"""
Multi-line comment
or docstring
"""
```

### Variables
```python
# No declaration needed
name = "Alice"
age = 30
height = 5.6
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0
```

### Indentation
Python uses indentation (4 spaces) to define code blocks.
```python
if True:
    print("Indented block")
    print("Still in block")
print("Outside block")
```

---

## Data Types

### Numeric Types
```python
# Integer
x = 10
y = -5

# Float
pi = 3.14159
temp = -40.5

# Complex
z = 2 + 3j

# Type conversion
int("42")      # 42
float("3.14")  # 3.14
str(100)       # "100"
```

### Boolean
```python
is_valid = True
is_empty = False

# Boolean operations
result = True and False  # False
result = True or False   # True
result = not True        # False
```

### None Type
```python
value = None  # Represents absence of value
```

---

## Operators

### Arithmetic Operators
```python
a, b = 10, 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulus = a % b         # 1
exponent = a ** b       # 1000
```

### Comparison Operators
```python
x, y = 5, 10

equal = x == y           # False
not_equal = x != y       # True
greater = x > y          # False
less = x < y             # True
greater_equal = x >= y   # False
less_equal = x <= y      # True
```

### Logical Operators
```python
and_op = (5 > 3) and (10 < 20)  # True
or_op = (5 > 3) or (10 > 20)    # True
not_op = not (5 > 3)            # False
```

### Assignment Operators
```python
x = 5
x += 3   # x = 8
x -= 2   # x = 6
x *= 4   # x = 24
x /= 3   # x = 8.0
x //= 2  # x = 4.0
x %= 3   # x = 1.0
x **= 2  # x = 1.0
```

---

## Control Flow

### If-Elif-Else
```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### For Loops
```python
# Iterate over sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range
for i in range(5):        # 0 to 4
    print(i)

for i in range(2, 10):    # 2 to 9
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# With else clause
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed")
```

### Break and Continue
```python
# Break: exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue: skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

### Pass Statement
```python
# Placeholder for future code
for i in range(5):
    pass  # Do nothing

def future_function():
    pass  # To be implemented
```

---

## Functions

### Defining Functions
```python
def greet(name):
    """Function with docstring"""
    return f"Hello, {name}!"

result = greet("Alice")  # "Hello, Alice!"
```

### Default Parameters
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27
```

### Keyword Arguments
```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(animal="dog", name="Rex")
describe_pet(name="Whiskers", animal="cat")
```

### Variable Number of Arguments
```python
# *args for positional arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs for keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
```

### Return Multiple Values
```python
def get_user():
    return "Alice", 30, "NYC"

name, age, city = get_user()
```

### Lambda Functions (Anonymous)
```python
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x, y: x + y
print(add(3, 4))  # 7
```

---

## Data Structures

### Lists (Mutable, Ordered)
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing elements
first = fruits[0]      # "apple"
last = fruits[-1]      # "cherry"
slice = fruits[0:2]    # ["apple", "banana"]

# Modifying lists
fruits.append("orange")         # Add to end
fruits.insert(1, "mango")       # Insert at index
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last
popped = fruits.pop(0)          # Remove and return at index
fruits.extend(["grape", "kiwi"]) # Add multiple items

# List operations
length = len(fruits)            # Length
fruits.sort()                   # Sort in place
fruits.reverse()                # Reverse in place
sorted_fruits = sorted(fruits)  # Return sorted copy
count = fruits.count("apple")   # Count occurrences
index = fruits.index("cherry")  # Find index

# List methods
fruits.clear()                  # Remove all items
shallow_copy = fruits.copy()    # Shallow copy
```

### Tuples (Immutable, Ordered)
```python
# Creating tuples
coordinates = (10, 20)
single = (1,)  # Note the comma
colors = "red", "green", "blue"  # Parentheses optional

# Accessing
x, y = coordinates  # Unpacking
first = colors[0]   # "red"

# Tuples are immutable
# coordinates[0] = 5  # TypeError!
```

### Dictionaries (Key-Value Pairs)
```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Another way
person = dict(name="Alice", age=30, city="NYC")

# Accessing values
name = person["name"]           # "Alice"
age = person.get("age")         # 30
age = person.get("salary", 0)   # 0 (default if not found)

# Modifying
person["age"] = 31              # Update
person["job"] = "Engineer"      # Add new key
del person["city"]              # Delete key
popped = person.pop("job")      # Remove and return

# Dictionary methods
keys = person.keys()            # All keys
values = person.values()        # All values
items = person.items()          # Key-value pairs

# Iterating
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

### Sets (Unique, Unordered)
```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Adding and removing
fruits.add("orange")
fruits.remove("banana")     # KeyError if not found
fruits.discard("grape")     # No error if not found
popped = fruits.pop()       # Remove arbitrary item

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b               # {1, 2, 3, 4, 5, 6}
intersection = a & b        # {3, 4}
difference = a - b          # {1, 2}
symmetric_diff = a ^ b      # {1, 2, 5, 6}

# Set methods
a.update(b)                 # Add all from b
is_subset = a.issubset(b)
is_superset = a.issuperset(b)
```

---

## String Manipulation

### Creating and Accessing Strings
```python
text = "Hello, World!"
multiline = """This is
a multiline
string"""

# Accessing
first_char = text[0]        # 'H'
last_char = text[-1]        # '!'
substring = text[0:5]       # "Hello"
```

### String Methods
```python
text = "  Hello, World!  "

# Case manipulation
upper = text.upper()           # "  HELLO, WORLD!  "
lower = text.lower()           # "  hello, world!  "
title = text.title()           # "  Hello, World!  "
capitalize = text.capitalize() # "  hello, world!  "

# Whitespace
stripped = text.strip()        # "Hello, World!"
lstripped = text.lstrip()      # "Hello, World!  "
rstripped = text.rstrip()      # "  Hello, World!"

# Searching
index = text.find("World")     # 9 (or -1 if not found)
count = text.count("l")        # 3
starts = text.startswith("  ") # True
ends = text.endswith("!  ")    # True

# Replacing
new_text = text.replace("World", "Python")

# Splitting and joining
words = "apple,banana,cherry".split(",")  # ["apple", "banana", "cherry"]
joined = "-".join(words)                  # "apple-banana-cherry"

# Checking
is_alpha = "abc".isalpha()       # True
is_digit = "123".isdigit()       # True
is_alnum = "abc123".isalnum()    # True
is_space = "   ".isspace()       # True
```

### String Formatting
```python
name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"
formatted = f"Pi is approximately {3.14159:.2f}"  # "Pi is approximately 3.14"

# format() method
message = "My name is {} and I'm {} years old".format(name, age)
message = "My name is {0} and I'm {1} years old".format(name, age)
message = "My name is {n} and I'm {a} years old".format(n=name, a=age)

# % operator (old style)
message = "My name is %s and I'm %d years old" % (name, age)
```

---

## Object-Oriented Programming

### Classes and Objects
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

print(dog1.bark())  # "Rex says Woof!"
print(dog2)         # "Buddy is 5 years old"
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())  # "Rex barks"
print(cat.speak())  # "Whiskers meows"
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

### Class Methods and Static Methods
```python
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def helper_function(x, y):
        return x + y

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # 2
print(MyClass.helper_function(5, 3))  # 8
```

### Property Decorators
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # 5
print(circle.area)    # 78.54
circle.radius = 10    # Using setter
```

---

## File Handling

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read lines into list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write (overwrites existing)
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append
with open("file.txt", "a") as file:
    file.write("Appended line\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file.txt", "w") as file:
    file.writelines(lines)
```

### Working with Paths
```python
import os

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

# Get file info
size = os.path.getsize("file.txt")
is_file = os.path.isfile("file.txt")
is_dir = os.path.isdir("folder")

# Create directory
os.makedirs("new_folder", exist_ok=True)

# List directory contents
files = os.listdir(".")

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")
```

### CSV Files
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading with DictReader
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["column_name"])

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "NYC"],
    ["Bob", 25, "LA"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

## Error Handling

### Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch all exceptions
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

### Try-Except-Else-Finally
```python
try:
    file = open("file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    # Runs if no exception occurred
    print("File read successfully")
finally:
    # Always runs
    file.close()
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(e)
```

### Custom Exceptions
```python
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
```

---

## Modules and Packages

### Importing Modules
```python
# Import entire module
import math
print(math.sqrt(16))

# Import specific items
from math import sqrt, pi
print(sqrt(16))

# Import with alias
import numpy as np
import pandas as pd

# Import all (not recommended)
from math import *
```

### Creating Your Own Module
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.PI)
```

### Common Built-in Modules
```python
# math - Mathematical functions
import math
print(math.ceil(4.3))    # 5
print(math.floor(4.7))   # 4
print(math.sqrt(16))     # 4.0

# random - Random number generation
import random
print(random.randint(1, 10))        # Random integer
print(random.choice([1, 2, 3, 4]))  # Random choice
print(random.random())              # Random float [0, 1)

# datetime - Date and time
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
tomorrow = now + timedelta(days=1)

# collections - Additional data structures
from collections import Counter, defaultdict, deque
counter = Counter([1, 1, 2, 3, 3, 3])  # {3: 3, 1: 2, 2: 1}

# json - JSON handling
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
parsed = json.loads(json_string)

# re - Regular expressions
import re
pattern = r'\d+'
matches = re.findall(pattern, "abc123def456")  # ['123', '456']
```

---

## List Comprehensions

### Basic List Comprehension
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
```

### Nested List Comprehension
```python
# 2D matrix
matrix = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Dictionary and Set Comprehensions
```python
# Dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
evens = {x for x in range(20) if x % 2 == 0}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

---

## Lambda Functions

### Basic Lambda
```python
# Lambda syntax: lambda arguments: expression
add = lambda x, y: x + y
print(add(3, 5))  # 8

square = lambda x: x ** 2
print(square(4))  # 16
```

### Lambda with Built-in Functions
```python
# map() - Apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# filter() - Filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# sorted() - Sort with custom key
words = ["apple", "pie", "zoo", "a"]
sorted_words = sorted(words, key=lambda x: len(x))
# ['a', 'pie', 'zoo', 'apple']
```

### Lambda with reduce
```python
from functools import reduce

# reduce() - Reduce sequence to single value
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# 120 (1*2*3*4*5)
```

---

## Decorators

### Function Decorators
```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function
```

### Decorators with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output (3 times):
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Practical Decorators
```python
import time

def timer(func):
    """Measure execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

def cache(func):
    """Simple memoization"""
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## Generators

### Creating Generators
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### Generator Expressions
```python
# Like list comprehension but with ()
squares_gen = (x ** 2 for x in range(10))

# Memory efficient for large sequences
sum_of_squares = sum(x ** 2 for x in range(1000000))
```

### Practical Generator Example
```python
def read_large_file(file_path):
    """Memory-efficient file reading"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def fibonacci_gen():
    """Infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci_gen()
first_10 = [next(fib) for _ in range(10)]
```

---

## Context Managers

### Using Context Managers
```python
# Automatic resource management
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed

# Multiple context managers
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

### Creating Context Managers
```python
from contextlib import contextmanager

@contextmanager
def timer_context():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start:.4f} seconds")

with timer_context():
    # Code to time
    sum(range(1000000))
```

### Custom Context Manager Class
```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None

with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")
```

---

## Working with JSON

### JSON Basics
```python
import json

# Python to JSON
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript"],
    "is_active": True
}

# Serialize to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)

# Write to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# JSON to Python
json_string = '{"name": "Bob", "age": 25}'
parsed = json.loads(json_string)
print(parsed["name"])  # "Bob"

# Read from file
with open("data.json", "r") as file:
    data = json.load(file)
```

---

## Important Built-in Functions

### Common Functions
```python
# len() - Length of sequence
print(len([1, 2, 3]))        # 3
print(len("hello"))           # 5

# range() - Generate sequence
list(range(5))                # [0, 1, 2, 3, 4]
list(range(2, 8))             # [2, 3, 4, 5, 6, 7]
list(range(0, 10, 2))         # [0, 2, 4, 6, 8]

# sum() - Sum of numbers
print(sum([1, 2, 3, 4]))     # 10

# min() and max()
print(min([3, 1, 4, 2]))     # 1
print(max([3, 1, 4, 2]))     # 4

# abs() - Absolute value
print(abs(-5))                # 5

# round() - Round number
print(round(3.14159, 2))     # 3.14

# sorted() - Return sorted list
print(sorted([3, 1, 4, 2]))  # [1, 2, 3, 4]

# reversed() - Reverse iterator
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# zip() - Combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# enumerate() - Index and value
for i, val in enumerate(["a", "b", "c"]):
    print(f"{i}: {val}")

# all() and any()
print(all([True, True, True]))   # True
print(any([False, False, True])) # True

# isinstance() - Check type
print(isinstance(5, int))        # True
print(isinstance("hi", str))     # True

# type() - Get type
print(type(5))                   # <class 'int'>
```

---

## Best Practices

### Code Style (PEP 8)
```python
# Use 4 spaces for indentation
# Use snake_case for variables and functions
user_name = "Alice"
def calculate_total():
    pass

# Use PascalCase for classes
class MyClass:
    pass

# Constants in UPPER_CASE
MAX_SIZE = 100
PI = 3.14159

# Limit lines to 79 characters
# Use blank lines to separate logical sections
```

### Pythonic Code
```python
# Good: Use 'in' for membership testing
if item in my_list:
    pass

# Good: Use enumerate instead of range(len())
for i, value in enumerate(my_list):
    print(f"{i}: {value}")

# Good: Use zip for parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Good: Use with for file handling
with open("file.txt") as f:
    content = f.read()

# Good: Use list comprehension when appropriate
squares = [x**2 for x in range(10)]

# Good: Use get() for dictionaries
value = my_dict.get(key, default_value)
```

### Error Handling
```python
# Be specific with exceptions
try:
    result = risky_operation()
except ValueError as e:
    handle_value_error(e)
except KeyError as e:
    handle_key_error(e)

# Don't use bare except
# Bad:
try:
    something()
except:  # Too broad
    pass

# Good:
try:
    something()
except Exception as e:
    logging.error(f"Error: {e}")
```

### Documentation
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The calculated area
    
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be positive")
    return length * width
```

### Performance Tips
```python
# Use list comprehensions over loops when possible
# Faster:
squares = [x**2 for x in range(1000)]
# Slower:
squares = []
for x in range(1000):
    squares.append(x**2)

# Use generators for large sequences
# Memory efficient:
sum(x**2 for x in range(1000000))

# Use sets for membership testing
# Fast:
items = set([1, 2, 3, 4, 5])
if 3 in items:  # O(1)
    pass

# Avoid repeated attribute lookup
# Faster:
append = my_list.append
for item in data:
    append(item)
```

---

## Conclusion

This tutorial covered the essential Python concepts and features. To continue learning:

1. Practice regularly by solving coding challenges
2. Build projects to apply what you've learned
3. Read Python documentation and PEPs (Python Enhancement Proposals)
4. Explore popular libraries: NumPy, Pandas, Requests, Flask/Django
5. Learn about virtual environments and package management (pip, venv)
6. Study testing frameworks (unittest, pytest)
7. Explore async programming (asyncio)

Python is a vast language with many more advanced features, but mastering these fundamentals will give you a solid foundation for any Python project.

Happy coding!