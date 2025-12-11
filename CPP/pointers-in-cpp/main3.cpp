#include <iostream>
using namespace std;

// int arr[]=int *arr in formal argument declaration
// all pointers are of same size i.e.. for 32 bit machine 4byte and for 64 bit machine 8byte
int sumOfElements(int arr[], int size) // we can also use int *arr insted of arr[] but arr[] increases readability
{
    //(arr) is the pointer to array
    // cout<<sizeof(arr)<<endl;//it gives warning that arr is a pointer and you expect it as whole array
    // arr++;//it is valid in this case of formal argument
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i]; // you can also write sum+=*(arr+i)
    }
    return sum;
}

void doubleArray(int *ptr, int size)
{
    for (int i = 0; i < size; i++)
    {
        *(ptr + i) = 2 * (*(ptr + i));
    }
}

void pointerPrint(int *ptr)
{                                                  // you can also use ptr[]
    cout << "the value of pointer is :" << ptr[0]; // you can also use *ptr
    return;
}
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = (sizeof(arr) / sizeof(arr[0]));
    cout << "sum of arr elements is :" << sumOfElements(arr, size) << endl; // arr can be replace by arr[0]
    doubleArray(arr, size);
    cout << "doubled array :" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }

    int ary[] = {2, 3, 1, 4}; // in this case we cant use ary as a pointer
    // ary++;//it is not valid in this case

    // if you really pass pointers then we can also use ptr[4] for *(ptr+i)
    int *point;
    int x = 10;
    point = &x;
    pointerPrint(point);

    return 0;
}