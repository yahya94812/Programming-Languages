// ============================================
// BASIC C++ TUTORIAL WITH EXAMPLES
// ============================================

#include <iostream>  // For input/output operations
#include <string>    // For string operations
#include <vector>    // For dynamic arrays

using namespace std;  // Use standard namespace

// ============================================
// 1. BASIC STRUCTURE & HELLO WORLD
// ============================================

void helloWorld() {
    // cout is used for output, endl adds a new line
    cout << "Hello, World!" << endl;
}

// ============================================
// 2. VARIABLES & DATA TYPES
// ============================================

void variablesAndTypes() {
    // Integer types
    int age = 25;           // Whole numbers
    long population = 1000000L;
    
    // Floating point types
    float price = 19.99f;   // Single precision
    double pi = 3.14159;    // Double precision (more accurate)
    
    // Character and boolean
    char grade = 'A';       // Single character
    bool isPassed = true;   // true or false
    
    // String (requires #include <string>)
    string name = "John";
    
    // Display values
    cout << "Name: " << name << ", Age: " << age << endl;
    cout << "Price: $" << price << ", Grade: " << grade << endl;
}

// ============================================
// 3. OPERATORS
// ============================================

void operators() {
    int a = 10, b = 3;
    
    // Arithmetic operators
    cout << "Addition: " << (a + b) << endl;        // 13
    cout << "Subtraction: " << (a - b) << endl;     // 7
    cout << "Multiplication: " << (a * b) << endl;  // 30
    cout << "Division: " << (a / b) << endl;        // 3 (integer division)
    cout << "Modulus: " << (a % b) << endl;         // 1 (remainder)
    
    // Comparison operators (return bool)
    cout << "Is a > b? " << (a > b) << endl;   // 1 (true)
    cout << "Is a == b? " << (a == b) << endl; // 0 (false)
    
    // Logical operators
    bool x = true, y = false;
    cout << "x AND y: " << (x && y) << endl;  // 0 (false)
    cout << "x OR y: " << (x || y) << endl;   // 1 (true)
    cout << "NOT x: " << (!x) << endl;        // 0 (false)
}

// ============================================
// 4. CONDITIONAL STATEMENTS
// ============================================

void conditionals() {
    int score = 85;
    
    // if-else statement
    if (score >= 90) {
        cout << "Grade: A" << endl;
    } else if (score >= 80) {
        cout << "Grade: B" << endl;
    } else if (score >= 70) {
        cout << "Grade: C" << endl;
    } else {
        cout << "Grade: F" << endl;
    }
    
    // Switch statement
    int day = 3;
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;  // Break prevents fall-through
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        default:
            cout << "Other day" << endl;
    }
}

// ============================================
// 5. LOOPS
// ============================================

void loops() {
    // For loop - used when you know iteration count
    cout << "For loop: ";
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";  // Prints: 1 2 3 4 5
    }
    cout << endl;
    
    // While loop - used when condition-based
    cout << "While loop: ";
    int j = 1;
    while (j <= 5) {
        cout << j << " ";
        j++;
    }
    cout << endl;
    
    // Do-while loop - executes at least once
    cout << "Do-while loop: ";
    int k = 1;
    do {
        cout << k << " ";
        k++;
    } while (k <= 5);
    cout << endl;
}

// ============================================
// 6. ARRAYS
// ============================================

void arrays() {
    // Fixed-size array
    int numbers[5] = {10, 20, 30, 40, 50};
    
    cout << "Array elements: ";
    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;
    
    // Multidimensional array
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    
    cout << "Matrix:" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

// ============================================
// 7. FUNCTIONS
// ============================================

// Function that returns a value
int add(int x, int y) {
    return x + y;
}

// Function with no return value (void)
void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

// Function with default parameter
int multiply(int a, int b = 2) {
    return a * b;
}

void functionsDemo() {
    int sum = add(5, 3);
    cout << "Sum: " << sum << endl;
    
    greet("Alice");
    
    cout << "Multiply: " << multiply(5) << endl;      // Uses default b=2
    cout << "Multiply: " << multiply(5, 4) << endl;   // Overrides default
}

// ============================================
// 8. PASS BY VALUE VS PASS BY REFERENCE
// ============================================

// Pass by value - creates a copy
void incrementValue(int x) {
    x++;  // Only changes the copy
}

// Pass by reference - works with original
void incrementReference(int &x) {
    x++;  // Changes the original variable
}

void passingDemo() {
    int num = 10;
    
    incrementValue(num);
    cout << "After pass by value: " << num << endl;  // Still 10
    
    incrementReference(num);
    cout << "After pass by reference: " << num << endl;  // Now 11
}

// ============================================
// 9. POINTERS
// ============================================

void pointers() {
    int value = 42;
    int *ptr = &value;  // ptr stores the address of value
    
    cout << "Value: " << value << endl;
    cout << "Address: " << &value << endl;
    cout << "Pointer: " << ptr << endl;
    cout << "Dereferenced pointer: " << *ptr << endl;  // Gets value at address
    
    // Modify through pointer
    *ptr = 100;
    cout << "New value: " << value << endl;  // 100
}

// ============================================
// 10. VECTORS (DYNAMIC ARRAYS)
// ============================================

void vectors() {
    // Vector - dynamic array that can grow/shrink
    vector<int> nums;
    
    // Add elements
    nums.push_back(10);
    nums.push_back(20);
    nums.push_back(30);
    
    cout << "Vector elements: ";
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    
    // Range-based for loop (C++11)
    cout << "Using range-based loop: ";
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
    
    // Remove last element
    nums.pop_back();
    cout << "After pop_back, size: " << nums.size() << endl;
}

// ============================================
// 11. CLASSES & OBJECTS (OOP)
// ============================================

class Rectangle {
private:
    // Private members - accessible only within class
    double width;
    double height;
    
public:
    // Constructor - called when object is created
    Rectangle(double w, double h) {
        width = w;
        height = h;
    }
    
    // Member functions (methods)
    double area() {
        return width * height;
    }
    
    double perimeter() {
        return 2 * (width + height);
    }
    
    // Getter methods
    double getWidth() { return width; }
    double getHeight() { return height; }
    
    // Setter methods
    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }
};

void classesDemo() {
    // Create object
    Rectangle rect(5.0, 3.0);
    
    cout << "Rectangle area: " << rect.area() << endl;
    cout << "Rectangle perimeter: " << rect.perimeter() << endl;
    
    // Modify using setters
    rect.setWidth(10.0);
    cout << "New area: " << rect.area() << endl;
}

// ============================================
// MAIN FUNCTION - PROGRAM ENTRY POINT
// ============================================

int main() {
    cout << "=== C++ TUTORIAL ===" << endl << endl;
    
    cout << "1. Hello World:" << endl;
    helloWorld();
    cout << endl;
    
    cout << "2. Variables & Types:" << endl;
    variablesAndTypes();
    cout << endl;
    
    cout << "3. Operators:" << endl;
    operators();
    cout << endl;
    
    cout << "4. Conditionals:" << endl;
    conditionals();
    cout << endl;
    
    cout << "5. Loops:" << endl;
    loops();
    cout << endl;
    
    cout << "6. Arrays:" << endl;
    arrays();
    cout << endl;
    
    cout << "7. Functions:" << endl;
    functionsDemo();
    cout << endl;
    
    cout << "8. Pass by Value vs Reference:" << endl;
    passingDemo();
    cout << endl;
    
    cout << "9. Pointers:" << endl;
    pointers();
    cout << endl;
    
    cout << "10. Vectors:" << endl;
    vectors();
    cout << endl;
    
    cout << "11. Classes & Objects:" << endl;
    classesDemo();
    
    return 0;  // Return 0 indicates successful execution
}