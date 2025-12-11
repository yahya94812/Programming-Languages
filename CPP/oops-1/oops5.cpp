#include <iostream>
#include <string>
using namespace std;

// inheritance
// when the properties or (attributes) and member function or (methods) of base class or (parent class) is passed on to the derived or (child class)
// if we made the obj of derived class then first parent class constructor is called

class Person
{
public:
    string name;
    int age;

    Person(string name, int age)
    {
        this->name = name;
        this->age = age;
    }
};

class Boy
{
public:
    int hight;
    Boy(int hight)
    {
        this->hight = hight;
    }
};

class Student : public Person, public Boy
{
public:
    int roll_no;
    Student(string name, int age, int hight, int roll_no) : Person(name, age), Boy(hight)
    {
        this->roll_no = roll_no;
    }

    void getInfo()
    {
        cout << name << endl;
        cout << age << endl;
        cout << hight << endl;
        cout << roll_no << endl;
    }
};

int main()
{
    Student s1("yahya", 19, 5, 76);
    s1.getInfo();

    return 0;
}