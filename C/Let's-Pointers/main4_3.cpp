#include<iostream>
using namespace std;

void print1d(int *A){//int A[]=int *A
    cout<<*A<<" "<<A[1]<<endl;//*A=A[0]
}

void print2d(int (*A)[2]){//int (*A)[2]=int A[][2] //where (*A) is type casting
    cout<<A[0][0]<<" "<<A[0][1]<<endl;//A[0][1]=*(*(A)+1)
}

void print3d(int (*A)[2][2]){//don't use ***A not work
    cout<<A[0][0][0]<<" "<<A[0][0][1]<<endl;
}
int main(){

    int A[2]={1,2};
    print1d(A);

    int B[2][2]={
                {1,2},
                {3,4}
    };
    print2d(B);//B is the address of first element which is 1d arry, of 2d therefore we use A[][2]//or B return an 1d array address (*p)[2]

    int C[3][2][2]={
            {1,2,
            3,4},//use ( , ) like this only don't use inside the {}

            {5,6,
            7,8},

            {9,10,
            11,12}
    };
    print3d(C);
    return 0;
}