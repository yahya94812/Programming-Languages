# sample user-defined module: calculator.py
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

# Module variable
PI = 3.14159

# Module-level code (runs when imported)
print(f"Calculator module loaded! PI = {PI}")

# This runs only when the module is executed directly
if __name__ == "__main__":
    print("Testing calculator module:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")