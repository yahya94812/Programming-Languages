"""
Python Basics Tutorial
A comprehensive guide to fundamental Python concepts
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Numbers
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print("=== Numbers ===")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# Strings
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is a
multi-line string"""

print("\n=== Strings ===")
print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"String concatenation: {single_quote + ' ' + double_quote}")
print(f"String repetition: {'Hi' * 3}")
print(f"String length: {len(single_quote)}")

# Boolean
is_true = True
is_false = False

print("\n=== Booleans ===")
print(f"True value: {is_true}")
print(f"False value: {is_false}")
print(f"Boolean from comparison: {10 > 5}")

# ============================================
# 2. COLLECTIONS
# ============================================

# Lists (mutable, ordered)
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]

print("\n=== Lists ===")
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
fruits.append("grape")
print(f"After append: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")

# Tuples (immutable, ordered)
coordinates = (10, 20)
rgb = (255, 128, 0)

print("\n=== Tuples ===")
print(f"Coordinates: {coordinates}")
print(f"X coordinate: {coordinates[0]}")
print(f"RGB values: {rgb}")

# Dictionaries (mutable, key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("\n=== Dictionaries ===")
print(f"Person dict: {person}")
print(f"Name: {person['name']}")
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

# Sets (mutable, unique elements, unordered)
unique_nums = {1, 2, 3, 3, 4}
programming_langs = {"Python", "Java", "JavaScript"}

print("\n=== Sets ===")
print(f"Unique numbers: {unique_nums}")
print(f"Programming languages: {programming_langs}")
programming_langs.add("C++")
print(f"After adding C++: {programming_langs}")

# ============================================
# 3. OPERATORS
# ============================================

print("\n=== Operators ===")

# Arithmetic operators
a, b = 10, 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Comparison operators
x, y = 5, 8
print(f"\nComparison: x={x}, y={y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x <= y: {x <= y}")

# Logical operators
p, q = True, False
print(f"\nLogical: p={p}, q={q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")

# ============================================
# 4. CONTROL FLOW
# ============================================

print("\n=== Control Flow ===")

# If-elif-else
score = 85
print(f"Score: {score}")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# For loops
print("\nFor loop - iterating through list:")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"  Color: {color}")

print("\nFor loop with range:")
for i in range(3):
    print(f"  Count: {i}")

print("\nFor loop with enumerate:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# While loop
print("\nWhile loop:")
counter = 0
while counter < 3:
    print(f"  Counter: {counter}")
    counter += 1

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(f"\nList comprehension:")
print(f"Original: {numbers}")
print(f"Squares: {squares}")

even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {even_numbers}")

# ============================================
# 5. FUNCTIONS
# ============================================

print("\n=== Functions ===")

# Basic function
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Bob"))

# Function with default parameter
def power(base, exponent=2):
    """Calculate base raised to exponent (default: 2)"""
    return base ** exponent

print(f"power(3): {power(3)}")
print(f"power(3, 3): {power(3, 3)}")

# Function with multiple returns
def calculate_stats(numbers):
    """Calculate sum and average of numbers"""
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

nums = [10, 20, 30, 40, 50]
total, average = calculate_stats(nums)
print(f"Numbers: {nums}")
print(f"Total: {total}, Average: {average}")

# Lambda function
square = lambda x: x ** 2
print(f"\nLambda function - square(5): {square(5)}")

# Map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
filtered = list(filter(lambda x: x > 2, numbers))
sum_all = reduce(lambda x, y: x + y, numbers)

print(f"Original: {numbers}")
print(f"Mapped (squared): {squared}")
print(f"Filtered (>2): {filtered}")
print(f"Reduced (sum): {sum_all}")

# ============================================
# 6. CLASSES AND OBJECTS
# ============================================

print("\n=== Classes and Objects ===")

class Dog:
    """Simple Dog class"""
    
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor method"""
        self.name = name  # Instance variable
        self.age = age
    
    def bark(self):
        """Method to make dog bark"""
        return f"{self.name} says Woof!"
    
    def describe(self):
        """Method to describe the dog"""
        return f"{self.name} is {self.age} years old"

# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.describe()}")
print(f"Dog 1 barks: {dog1.bark()}")
print(f"Dog 2: {dog2.describe()}")
print(f"Species: {Dog.species}")

# Inheritance
class Puppy(Dog):
    """Puppy class inheriting from Dog"""
    
    def __init__(self, name, age, training_level):
        super().__init__(name, age)
        self.training_level = training_level
    
    def play(self):
        return f"{self.name} is playing!"

puppy = Puppy("Charlie", 1, "beginner")
print(f"\nPuppy: {puppy.describe()}")
print(f"Puppy plays: {puppy.play()}")

# ============================================
# 7. EXCEPTION HANDLING
# ============================================

print("\n=== Exception Handling ===")

# Basic try-except
try:
    result = 10 / 2
    print(f"10 / 2 = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions and else
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types for division"
    else:
        return f"Result: {result}"
    finally:
        print("Division operation completed")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# ============================================
# 8. FILE OPERATIONS
# ============================================

print("\n=== File Operations (Examples) ===")

# Writing to file (example - not executed)
example_write = """
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    file.write('\\nPython is awesome!')
"""
print("Writing to file:")
print(example_write)

# Reading from file (example - not executed)
example_read = """
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
"""
print("\nReading from file:")
print(example_read)

# ============================================
# 9. MODULES AND IMPORTS
# ============================================

print("\n=== Modules and Imports ===")

import math
import random
from datetime import datetime

print(f"Math.pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number (1-10): {random.randint(1, 10)}")
print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================
# 10. USEFUL BUILT-IN FUNCTIONS
# ============================================

print("\n=== Useful Built-in Functions ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sorted: {sorted(numbers)}")
print(f"Reversed: {list(reversed(numbers))}")

# Type conversion
num_str = "123"
print(f"\nType conversion:")
print(f"String '{num_str}' to int: {int(num_str)}")
print(f"Int 456 to string: {str(456)}")
print(f"String '3.14' to float: {float('3.14')}")

# Zip function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"\nZip function:")
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Zipped: {combined}")

# Any and all
bool_list = [True, True, False]
print(f"\nBoolean operations on {bool_list}:")
print(f"Any true? {any(bool_list)}")
print(f"All true? {all(bool_list)}")

print("\n" + "="*50)
print("Python Basics Tutorial Complete!")
print("="*50)