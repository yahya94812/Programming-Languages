# Types of Modules
# Built-in modules: Come with Python installation (like math, os, datetime)
# User-defined modules: Created by you
# Third-party modules: Installed via pip (like requests, numpy)

# Module naming: Use lowercase with underscores (snake_case)
# File name should match module name (e.g., calculator.py for calculator module)

# Different ways to import and use modules
# 1. Import entire module
import calculator
result1 = calculator.add(10, 5)
print(f"Using calculator.add(): {result1}")
print(f"PI from module: {calculator.PI}")

# 2. Import specific functions
from calculator import add, subtract, PI
result2 = add(20, 30)
result3 = subtract(40, 15)
print(f"Using imported add(): {result2}")
print(f"Using imported subtract(): {result3}")
print(f"PI: {PI}")

# 3. Import with alias
import calculator as calc
result4 = calc.subtract(100, 25)
print(f"Using aliased module: {result4}")

# 4. Import all (use sparingly)
# from calculator import *
# This imports all functions and variables

# 5. Import with function alias
from calculator import subtract as sub
result5 = sub(50, 10)
print(f"Using aliased function: {result5}")