#include <iostream>
#include <string>
using namespace std;

// you can't copy dynamically allocated memory using shallow copy as it copy only member variables

class Student
{
public:
    string name; // member variables
    int rollNo;
    int *marksPtr;

    Student(string name, int rollNo, int marks) // this are local scope var and it is like a function
    {
        this->name = name;
        this->rollNo = rollNo;
        marksPtr = new int;
        *marksPtr = marks; // if the parameter's names and member values name are different we can write it without (this->)
        // this stores the marks as the value of marksPtr but if we use {marksPtr=&marks} then marksPtr is store the address of mark variable which is cause error probably
    }

    Student(Student *student)
    { // this is custom deep copy constructor
        name = student->name;
        rollNo = student->rollNo;
        marksPtr = new int;
        *marksPtr = *(student->marksPtr);
    }

    void printDetail()
    {
        cout << "---DETAILS---" << endl;
        cout << name << endl
             << rollNo << endl
             << *marksPtr << endl; // there is not compulsory to write this-> for accessing the member variables
        // use *(this->marks) as this->*marks does't work
    }
};

int main()
{
    Student s1("yahya", 76, 100);
    cout << "details of student1" << endl;
    s1.printDetail();

    // Student s2(s1);//default copy
    Student s2(&s1); // it is custom deep copy constructor
    cout << "details of student2" << endl;
    s2.printDetail();

    *(s2.marksPtr) = 80; // if i changed one object variable it does't change other object variable

    cout << "details of student2" << endl;
    s2.printDetail();

    cout << "details of student1" << endl;
    s1.printDetail();

    return 0;
}
