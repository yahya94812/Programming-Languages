#include <iostream>
using namespace std;

class Student
{
public:
    string *name;
    int *marks;
    Student(string name, int marks)
    { // this is constructor which called automatically when the object is created
        this->name = new string;
        this->marks = new int;
        *(this->name) = name;
        *(this->marks) = marks;
    }

    ~Student()
    { // it is invoked when the object is destroyed or the object is go out of scope if not use may memory leak condition arises; and it is used to delete the dynamically allocated variables
        cout << "i am in destructor" << endl;
        delete name;
        delete marks;
        cout << "member variables are destroyed" << endl;
    }
};

int main()
{
    Student s1("yahya", 100);
    cout << *(s1.name) << endl;
    cout << *(s1.marks) << endl;

    return 0;
}