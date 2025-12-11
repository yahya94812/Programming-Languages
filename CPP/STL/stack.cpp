#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> my_stack;

    my_stack.push(10);
    cout<< my_stack.top()<<endl;
    cout<< my_stack.size()<<endl;
    cout<< my_stack.empty()<<endl;
    my_stack.pop(); //it return void

    return 0;
}