// In C++, references are essentially aliases for existing variables. They allow you to access and modify the original variable using a different name. 
// A reference must be initialized when it's declared.
// Once set, a reference cannot be changed to refer to a different variable.
// A reference is not a copy of the variable; it is another name for the same memory location.

#include <iostream>
using namespace std;

void update(int&);

int main(){
    int x = 10;
    int& ref = x;
    ref = 20;

    cout<<x<<endl;

    update(x);

    cout<<x<<endl;

    return 0;
}

void update(int& val){ 
    //it avoid copying and allow modification
    val += 5;
}

int& get_element(int arr[], int index){
    //(to return an actual variable, not a copy
    return arr[index];
}

void print(const int& val){
    //To refer to something without modifying it
    cout << val;
}