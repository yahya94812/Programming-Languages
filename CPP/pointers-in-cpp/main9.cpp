#include <iostream>
#include <stdlib.h>
using namespace std;

int* Add(int *a, int *b){//bad practice
    int c = *a+*b;
    //insted use heap//very good practice
    //c=(int*)malloc(sizeof(int));
    //*c=*a+*b;
    //return c;
    return &c;
}

int main(){
    int x = 0, y = 0;//cause warning and not guaranteed especially after calling other functions as the same portion of stack is taken by other functions
    int *padd=Add(&x,&y);
    cout<<"x = "<<x<<endl;
    //we can't define the size of array at run time (by inputing a variables) as the memory is allocated only at compile time
    //for array of variable size
    int varSize;
    cout<<"enter the size of array"<<endl;
    cin>>varSize;
    int *p;
    // p=(int*)malloc(varSize*sizeof(int));//initialize elements of array as garbage values
    p=new int[varSize*sizeof(int)];//dynamically allocated array 
    // p=(int*)calloc(varSize, sizeof(int));//return Array in which all elements are zero
    for(int i=0;i<varSize;i++){
        p[i]=i+1;
    }
    for(int i=0;i<varSize;i++){
        cout<<p[i]<<" ";
    }
    cout<<endl;
    delete[] p; //use [] for delete an array
    // p=NULL;//use it for previnting any errors
    p[3]=23;

    for(int i=0;i<varSize;i++){
        cout<<p[i]<<" ";//return garbage values and p[3] is 23 and there is no guarantee for it if we call any function
    }
    cout<<endl;

    //therefore set p to NULL for preventing errors

    //int *p=(int*)realloc(NULL,sizeof(int)); //equivalent to malloc and if NULL is ptr and sizeof(int) is 0 then it is equivalent to free()

    //never declare any pointers in called function because if that function is executed and returns then all the values that are pointed by that pointer will be cleared (or stay there only) if any other function is take the same stack portion which the previous function was taken then all values will be cleared
    //never try to return a pointer from a called function when it is declared in that function only

    return 0;
}