# Python Basics Tutorial
# This script covers fundamental Python concepts for beginners

# ----- 1. Variables and Basic Data Types -----
print("1. Variables and Basic Data Types")

# Integers, Floats, and Strings
age = 25                # Integer
height = 5.9            # Float
name = "John Doe"       # String
is_student = True       # Boolean

print(f"Name: {name}, Age: {age}, Height: {height}ft, Student: {is_student}")

# Type checking
print(f"Variable types: {type(name)}, {type(age)}, {type(height)}, {type(is_student)}")

# ----- 2. Basic Operations -----
print("\n2. Basic Operations")

# Arithmetic operations
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus (remainder): {a % b}")
print(f"Exponentiation: {a ** b}")

# String operations
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name  # Concatenation
print(f"Full name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Length: {len(full_name)}")

# ----- 3. Lists -----
print("\n3. Lists")

# Creating and accessing lists
fruits = ["apple", "banana", "cherry", "orange"]
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two fruits: {fruits[0:2]}")

# List operations
fruits.append("grape")         # Add item
fruits.insert(1, "blueberry")  # Insert at position
fruits.remove("cherry")        # Remove item
popped_fruit = fruits.pop()    # Remove and return last item
print(f"After modifications: {fruits}")
print(f"Popped fruit: {popped_fruit}")
print(f"List length: {len(fruits)}")

# ----- 4. Dictionaries -----
print("\n4. Dictionaries")

# Creating and accessing dictionaries
person = {
    "name": "Sarah Johnson",
    "age": 32,
    "occupation": "Software Engineer",
    "skills": ["Python", "JavaScript", "SQL"]
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"First skill: {person['skills'][0]}")

# Dictionary operations
person["location"] = "San Francisco"  # Add new key-value pair
person["age"] = 33                   # Modify existing value
print(f"After modifications: {person}")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")

# ----- 5. Conditional Statements -----
print("\n5. Conditional Statements")

x = 15

if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 but not greater than 20")
else:
    print("x is not greater than 10")

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# ----- 6. Loops -----
print("\n6. Loops")

# For loop with range
print("For loop with range:")
for i in range(1, 5):
    print(f"  Number: {i}")

# For loop with list
print("For loop with list:")
for fruit in fruits[:3]:  # First 3 fruits
    print(f"  Fruit: {fruit}")

# While loop
print("While loop:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1

# ----- 7. Functions -----
print("\n7. Functions")

# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def calculate_area(length, width=1):
    return length * width

print(greet("Alice"))
print(f"Rectangle area: {calculate_area(5, 3)}")
print(f"Line length: {calculate_area(10)}")  # Using default width

# ----- 8. Exception Handling -----
print("\n8. Exception Handling")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")

# ----- 9. Classes and Objects -----
print("\n9. Classes and Objects")

class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Create objects
buddy = Dog("Buddy", 5)
max = Dog("Max", 3)

print(buddy)
print(max.bark())
print(f"Both dogs are {Dog.species}")

# ----- 10. List Comprehensions -----
print("\n10. List Comprehensions")

# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Filter list using conditions
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")
