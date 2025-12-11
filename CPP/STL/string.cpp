#include <iostream>
#include <string>
using namespace std;

int main(){
    string str = "hello";
    str += " world";

    cout<<str<<endl;
    cout<<str.length()<<endl;
    cout<<str.substr(1, 3)<<endl;
    cout<<str.find("wor")<<endl;
    str.push_back('!'); //push only a char
    str.pop_back();

    int num = stoi("1234"); //stoi: string to int
    cout<<num<<endl;
    string str1 = to_string(1234);
    cout<<str1<<endl;

    return 0;
}