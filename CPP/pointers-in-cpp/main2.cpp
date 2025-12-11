#include <iostream>
using namespace std;

// local variables are the variables that have local scope and it is forgotten if the control exit from that function
// but if one function call another function the parents functions local variable remains as in recursion
// there are two type of function 1.call by value(simple) 2.call by reference(in which pointers are passed as arguments)
// when any program run there are 4 type of memory from ram alloted to program
// 1.heap: it is the type of memory that are allocated at run time of any program by the amount as needed
// 2.stack: in this each function is allocated a fix amount of memory at compile time for every function the stack frame is allocated in stack in which function's local variables are exist if the control return from any function the stack frame of that function are cleared(deleted)
// 3.global or static: in this memory all global variables and constants are stored
// 4.code(text): in this all the code instructions are stored
// for simple functions (not call by reference) calling function have actual arguments where the called function have formal arguments(parameters)

void increment(int *num)
{
    *num = *num + 1;
    return;
}
int main()
{
    int x = 10;
    cout << x << endl;
    increment(&x); // as the main function stack is remain even if the increment function is called therefore the increment function able to increment the variables of main function
    cout << x << endl;

    // POINTERS AND ARRAYS
    int arr[] = {1, 2, 3, 4, 5};
    cout << sizeof(arr) << endl; // out 4*5
    int *p;
    p = &arr[0];
    // or p=arr it is also called the base address
    // p=arr is necessary because we can't use (arr) directly as it cause error (lookup table) if we use arr++ or etc
    for (int i = 0; i < 5; i++)
    {
        cout << "value at address :" << p << " is " << *p << endl;
        p++;
        // or we can use p=p+2 for even index
        // for element at index i is arr[i] or *(arr + i)
        // for address of element at index i is (arr+i) or &arr[i]
    }

    return 0;
}