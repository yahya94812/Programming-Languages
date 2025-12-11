#include <iostream>
using namespace std;

// pointers store the address of other variables as their values
// we define the pointer types as int or float etc because it used to retrieve the value at this address consider if we define char *c; int num; c=&num and if i want to get value of num using pointer c i.e..;*c but i can't got a proper value of int because the pointer variable can store only the starting memory address where the type of pointer determine the size or length of data type and to how much span of this data type from starting memory address to retrieve it's value and how to get value from binary

int main()
{

    // declaration of pointer
    int *ptr1, *ptr2; // consider (int*) the data type for declaring integer pointer or normally int *ptr1, as *ptr1 is int
    // if ptr is any pointer then *ptr is integer therefore int *ptr is used for declaring pointer ptr

    // initialization of pointer
    int p1 = 1, p2 = 2;
    ptr1 = &p1;
    ptr2 = &p2;

    cout << ptr1 << " and " << ptr2 << endl;
    cout << "value of the above pointers are: " << endl
         << *ptr1 << " and " << *ptr2 << endl;

    *ptr1 = 3; // ptr1 value is not change but p1 value is changed
    cout << ptr1 << " and " << ptr2 << endl;
    cout << "value of the above pointers is: " << *ptr1 << " and " << *ptr2 << endl;
    // that means ptr and *ptr are two different variables

    // declaration with initialization {bad practice}
    int *ptr3 = &p1, *ptr4 = &p2;
    cout << ptr3 << " and " << ptr4 << endl;

    // we can find the size of any data type with sizeof() operator
    cout << sizeof(int) << " is the size of int in bytes" << endl;

    // every memory address is for 1byte of memory
    // the Look up table in c++ used to store variable name along with it's type and the first memory address  eg:if we define int a=5 then look up table is set up which contain {a int 204(memory add)} in our program if we use (a) then first it search a in look up table and get memory address and data type of a and then retrieve value of a from memory(RAM) OR int pointer say Look after 4 byte from starting

    int a;
    cout << a << endl; // garbage value
    int *p; //here p is a variable stores pointer
    cout << p << endl;  // garbage address as a value of p
    // cout << *p << endl; // value {may be any usefull value for os or unoccupied} at garbage address but os detect some unauthorize activity and terminate the program

    // pointer arithmetic
    int *pt;
    int ab = 10;
    pt = &ab;
    cout << pt << endl;
    pt++; // value of pt is incremented by 4 because it is int pointer if it is char pointer it's value is incremented by 1 only
    cout << pt << endl;
    cout << *pt << " is garbage value next ot ab value in memory" << endl;

    // type casting of pointers
    int num1 = 1025; // in this first 2 bytes are used for storing value {00000100 00000001}
    int *ptrn;
    ptrn = &num1;
    cout << ptrn << endl;
    cout << *ptrn << "=" << num1 << endl; //*ptrn look 4 byte from ptrn
    char *ptrc;
    ptrc = (char *)ptrn;                                  // type casting of int to char pointer
    cout << *ptrc << " is the value of char" << endl;     //*ptrc look only 1 byte from ptrc
    cout << int(*ptrc) << " is the value in int" << endl; // it is the value of first byte
    ptrc++;
    cout << int(*ptrc) << " is the value at second byte " << endl;

    // void pointer or generic pointer
    int iv;
    void *pv;
    int *nv;
    nv = &iv;
    pv = nv; // no need of (*void)
    // cout<<*pv<<endl; error can't use *pv
    cout << pv << "=" << nv << endl;
    // pv++;warning

    int x = 5;
    int *px;
    px = &x;
    int **pp;
    pp = &px;
    int ***r;
    r = &pp;
    cout << "value of x is :" << x << "=" << *px << "=" << **pp << "=" << ***r << endl;
    cout << "pointer of x is :" << &x << "=" << px << "=" << *pp << "=" << **r << endl;
    // int *temp; //same effect as below
    // temp=&x;
    // we can use multiple (*) like **** but we can't use multiple (&) because consider &&x this means find or give the variable address that store the address of x, in whole memory (it can be done with searching algorithm); where the multiple (*) which mean value at pointer which is again pointer to some value and so on
    int *temp = &x;                                                                                   // you can't use &(&x) because &x in this expression is not a variable then &(&x) is in valid mean we try to get address which is not a variable
    cout << "pointer to pointer of x is :" << &temp << "!=" << &px << "=" << pp << "=" << *r << endl; // this is because temp is other variable
    **pp = *px + 2;
    cout << x << endl;

    return 0;
}