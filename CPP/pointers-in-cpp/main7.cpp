#include <iostream>
using namespace std;

//3d array is the array of 2d array
int main(){

    int A[3][2][2]={
        {
            {1, 2},
            {3, 4}
        },
        {
            {5, 6},
            {7, 8}
        },
        {
            {9, 1},
            {2, 3}
        }
    };

    int (*p)[2][2]=A;
    cout<<A<<endl;//print the base of 3d array
    cout<<*A<<" or "<<A[0]<<" or "<<&A[0][0]<<endl;//all of these return the address of first 1d array of first 2d array of parent array of type int(*)[2]
    //A[i][j][k]=*(A[i][j]+k)=*(*(A[i]+j)+k)=*(*(*(A+i)+j)+k)
    cout<<*(A[0][0]+1)<<" or "<<A[0][0][1]<<endl;
    cout<<*(A[0]+1)<<" or "<<A[0][1]<<" or "<<&A[0][1][0]<<endl;
    
    return 0;
}