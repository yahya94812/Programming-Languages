#include <iostream>
using namespace std;

int main()
{
    //*(A+i) is same as A[i]
    //(A+i) is same as &A[i]
    // if A is array and p is int pointer then (p=A) is correct but (A=p) is not correct

    // 2d array can be consider as array of array
    // A[2][3]; means it is the array of 2 1d arrays which contain 3 integer each

    int A[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    // int *pn=A;//error becaus it return pointer to it's first element means first array &A[0]

    int (*p)[3] = A; // it receive the pointer to array of 3 elements

    cout << A << " = " << &A[0][0] << endl; // where A return pointer to array and A[0][0] return pointer to int
    cout << *A << " = " << A[0] << " = " << &A[0][0] << endl;
    cout << A + 1 << " or " << A[1] << " or " << &A[1] << endl;
    cout << *(A + 1) << " or " << A[1] << " or " << &A[1][0] << endl; // it return the pointer of int * or all are the name of second array element in parent array
    cout << *(*(A + 1)) << " or " << *(A + 1)[0] << endl; // here *(A+1) represent the name of second array element of parent array
    cout << A[1] + 2 << " or " << *(A + 1) + 2 << " or " << &A[1][2] << endl; // here the A[1] or *(A+1) is the name or base address of second element array
    cout << *(*A + 2) << " or " << A[0][2] << endl; // the A is int (*)[3] and A[1] is int*
    // A[i][j]=*(A[i] + j) or *(*(A+i)+j)
    // int (*p)[3]=A it is the pointer of 1d array of 3 element
    cout << *A << " " << A << " " << A[0] << " " << &A[0][0] << endl;

    return 0;
}