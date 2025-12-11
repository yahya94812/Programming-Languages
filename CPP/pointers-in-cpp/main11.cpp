#include <iostream>
using namespace std;

void A(){
    cout << "Function A called" << endl;
}

void B(void (*func_ptr_of_A)()){
    func_ptr_of_A();
}
int main() {
    //function pointers can be passed to other functions as arguments
    //A callback function is a function that is passed as an argument to another function and is expected to be executed (or "called back") at a certain point during the execution of that outer function

    void (*ptr)();
    ptr = A; //assigning address of A function to ptr
    B(ptr);//or B(A)//if i call function B with the argument of pointer of A then function A will be executed (or "called back") at a certain point during the execution

    //memory leak is the condition in which the heap is not cleared and the waste data is stay on the heap until the program terminates
    
    return 0;
}