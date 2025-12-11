#include <iostream>
#include <stdlib.h>

using namespace std;
int total; // it is a global variable not in stack
// in all cpp programs the main function is stay in the bottom of stack if main call any function then function form at the top of main function if this function returned, the stack frame of that function will be cleared
// heap is free pool of memory
// malloc
// calloc
// realloc
// free functions

// in C++
// new and delete operator

int main()
{
    int num; // in stack
    int *p;
    // p=(int *)malloc(sizeof(int));//memory allocation in heap (dynamic memory allocation), malloc return void pointer and argument is unsign pointer (int *) is type casting
    p = new int; // in cpp
    *p = 42;
    cout << *p << endl;
    *p = 24;
    cout << *p << endl;
    // free(p);//deallocate memory
    delete p;           // in cpp
    cout << *p << endl; // garbage value

    // for array
    //  p=(int *)malloc(20*sizeof(int));
    p = new int[20];
    for (int i = 0; i < 20; i++)
    {
        p[i] = i;
    };
    cout << p[5] << endl;
    // free(p);
    delete[] p;
    cout << p[5] << endl;

    // calloc
    int *ptr;
    ptr = (int *)calloc(3 /*no of elements*/, sizeof(int) /*size of elements*/); // same as malloc but initialize all the values as 0
    for (int i = 0; i < 3; i++)
    {
        cout << ptr[i] << endl;
    }

    // realloc
    p = (int *)realloc(ptr /*previous pointer*/, 5 * sizeof(int) /*size of new space*/); // increase or decrease the size of contiguous memory, it can copy all elements of previous array to new location if there is no contiguous memory
    for (int i = 0; i < 5; i++)
    {
        p[i] = i;
        cout << p[i] << endl;
    }
    
    return 0;
}