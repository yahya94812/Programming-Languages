// Run-time Polymorphism (Function Overriding)
// The const after the method name means: This method does not modify the object it is called on.

#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() const {
        return 0.0;
    }
    
    virtual void draw() const {
        cout << "Drawing a shape" << endl;
    }
};

class Circle : public Shape {
    // means that Circle is inheriting from the Shape class using public inheritance.
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing a circle" << endl;
    }
};

class Rectangle : public Shape {
private:
    double width;
    double height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    void draw() const override {
        cout << "Drawing a rectangle" << endl;
    }
};

void printArea(const Shape& shape) {
    // const Shape& shape — The function takes a reference to a Shape object, and that object is constant, meaning it cannot be modified inside the function.
    cout << "Area: " << shape.area() << endl;
    shape.draw();
}

int main() {
    Circle circle(5.0);
    Rectangle rectangle(4.0, 6.0);
    
    printArea(circle);     // Uses Circle's area() and draw()
    printArea(rectangle);  // Uses Rectangle's area() and draw()
    
    return 0;
}