#include <iostream>
using namespace std;

// Polymorphism is the ability of objects to take on different forms or behave in different way depending on the context in which they are used
// compile time polymerization eg. constructor or function overloading
// run time (dynamic) polymerization eg. virtual function(function overriding)
// Function Overriding : it is used in inheritance
// Parent & Child both contain the same function with different implementation The parent class function is said to be overridden.
// Virtual Functions :
// A virtual function is a member function that you expect to be redefined in derived classes. this is for run time polymerization

void func1(int a)
{
    cout << "func with one parameter" << endl;
}
// this is function overloading we can use different no. of parameter or parameter of different type and it can be use methods in classes
void func2(int a, int b)
{
    cout << "func with two parameter" << endl;
}

class A
{
public:
    A()
    {
        cout << "i am in non parameterize constructor" << endl;
    }
    // this is constructor overloading
    A(int x)
    {
        cout << "i am in parameterize constructor" << endl;
    }
};

class Parent
{
public:
    void getinfo()
    {
        cout << "i am in parent class" << endl;
    }
};
class Child : public Parent
{
public:
    void getinfo()
    {
        cout << "i am in children class" << endl;
    }
};

int main()
{

    A a;
    A b(1);

    func1(1);
    func2(1, 2);

    string str = "yahay";
    string str2 = str; // it is operator overloading

    Child ch;
    ch.getinfo(); // function overriden and in favor of child class
    Parent par;
    par.getinfo();
    
    return 0;
}