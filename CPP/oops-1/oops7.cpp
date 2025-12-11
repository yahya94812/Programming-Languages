#include <iostream>
using namespace std;

// Hiding all unnecessary details & showing only the important parts

// Abstract classes are used to provide a base class from which other classes can be derived.
// They cannot be instantiated and are meant to be inherited.
// Abstract classes are typically used to define an interface for derived classes.
// Abstraction is may be done by using access modifier

class shape
{ // abstract class by using atleast one virtual function
public:
    virtual void draw() = 0; // pure virtual function and it use to strictly declare member function to override it
};

class circle : public shape
{
public:
    void draw()
    {
        cout << "drawing circle\n";
    }
};

int main()
{
    circle c1;
    c1.draw();

    return 0;
}