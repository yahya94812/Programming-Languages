#include <iostream>
#include <string>
using namespace std;

//<this> is the special type of pointer that refer to the current obj in the class
// this->prop = *(this).porp
class Student
{
public:
    string name;
    int rollNo;
    int marks;

    // //non parameterized
    // Student(){
    //     cout<<"this is constructor"<<endl;
    // }

    // parameterized
    Student(string name, int rollNo, int marks)
    { // same as function definition
        this->name = name;
        this->rollNo = rollNo;
        this->marks = marks;
    }

    Student(Student *other)
    {                               // custom copy constructor
        this->name = (*other).name; // same thing as this->name
        this->rollNo = other->rollNo;
        this->marks = other->marks;
    }

    void printDetail()
    {
        cout << "DETAILS" << endl;
        cout << this->name << endl << this->rollNo << endl << this->marks << endl;
    }
};

int main()
{
    // Student s1;//it uses non parameterize constructor (polymorphism)

    Student s2("yahya", 76, 100);
    cout << "details of student2" << endl;
    s2.printDetail();

    // Student s3(s2); //simple and default copy constructor is called (shallow copy constructor) if not custom copy constructor is defined
    // cout << "details of student3" <<endl;
    // s3.printDetail();

    Student s4(&s2); // custom copy constructor is invoked
    cout << "details of student4" << endl;
    s4.printDetail();

    // a shallow copy is the copy of just all the properties of one object to other object
    // but the deep copy is the copy of not just the properties but the attributes that are pointing to other objects and values are also copied and it is used for the dynamic memory allocation as the new dynamic memory allocation is occur by the deep copy method

    return 0;
}