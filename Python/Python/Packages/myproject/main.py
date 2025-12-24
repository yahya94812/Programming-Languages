# Package structure:
# myproject/
# ├── __init__.py
# ├── utilities/
# │   ├── __init__.py
# │   ├── math_utils.py
# │   └── string_utils.py
# └── main.py
# main.py - Using the package

from utilities import factorial, fibonacci, reverse_string
from utilities.math_utils import factorial as fact

# Using imported functions
print(f"Factorial of 5: {factorial(5)}")
print(f"First 8 Fibonacci numbers: {fibonacci(8)}")
print(f"Reversed string: {reverse_string('Hello World')}")

# Using aliased function
print(f"Factorial of 6: {fact(6)}")

# Import entire submodule
import utilities.string_utils as str_utils
print(f"Capitalized: {str_utils.capitalize_words('hello python world')}")