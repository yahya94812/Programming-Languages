// C++ templates allow you to write code that works with any data type
// There are two main types:
// 1. Function Templates
// 2. Class Templates

#include <iostream>
using namespace std;

// function template
template <typename T> // declaration of a template in C++; it tells the compiler: "The following function or class will use a generic type named T, and the actual type will be specified when the template is used."
T getMax(T a, T b)
{
    return (a > b) ? a : b;
}

// template <class T> interchangeble with template <typename T>
template <typename T>
class Box
{
private:
    T value;

public:
    Box(T v) : value(v) {}

    T getValue(){
        return value;
    }
};

int main()
{
    // using function template
    cout << getMax<int>(3, 7) << endl; // here the <int> replace all the occurrence of T in function, not necessary to write <int> in front of function name while calling because compiler get to know it's datatypes form passed parameters
    cout << getMax<double>(3.4, 5.3) << endl;
    cout << getMax<char>('a', 'z') << endl;

    // using class template
    Box<int> intBox(123);
    Box<string> strBox("hello template");

    cout << intBox.getValue() << endl;
    cout << strBox.getValue() << endl;

    return 0;
}
