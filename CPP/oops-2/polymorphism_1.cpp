// Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables you to work with objects of different types through a uniform interface.
// Compile-time Polymorphism (Function Overloading)
// decision about which method to call is made at compile time, not runtime even if the object is created at runtime, compile some how identify which method object can call.

#include <iostream>
using namespace std;

class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
};

int main(){
    Calculator my_calculator;
    cout<<"3+4="<<my_calculator.add(3, 4)<<endl;
    cout<<"3.1+4.1="<<my_calculator.add(3.1, 4.1)<<endl;
    cout<<"3+4+1="<<my_calculator.add(3, 4, 1)<<endl;

    return 0;
}