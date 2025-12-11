#include <iostream>
using namespace std;

class MyClass
{
public:
    static int count; // Declaration of static variable

    MyClass()
    {
        count++; // Increment the static variable count whenever a new object is created
    }

    void displayCount()
    {
        cout << "Count: " << count << endl;
    }
};

int MyClass::count = 0;// you cannot initialize a static data member inside the class definition directly. 


//use of :: it is use for defining scope of a variables
int x = 10; // Global variable
void func() {
    int x = 20; // Local variable
    cout << "Local x: " << x << endl;        // Prints 20
    cout << "Global x: " << ::x << endl;     // Prints 10 using scope resolution operator
}

//static in normal function
void counter()
{
    static int count = 0; // This variable is initialized only once
    count++; // Increment the value of count
    cout << "Function called " << count << " times\n";
}


class ABC {
public:
    ABC() {
        cout << "constructor\n";
    }

    ~ABC() {
        cout << "destructor\n";
    }
};

int main()
{
    MyClass obj1;
    obj1.displayCount(); // Count: 1

    MyClass obj2;
    obj2.displayCount(); // Count: 2

    MyClass obj3;
    obj3.displayCount(); // Count: 3


    counter(); // First call, count is 1
    counter(); // Second call, count is 2
    counter(); // Third call, count is 3


    if (true) {
        static ABC obj;//see first main func end and then the ABC obj destructed 
    }

    cout << "end of main fnc\n";

    return 0;
}
