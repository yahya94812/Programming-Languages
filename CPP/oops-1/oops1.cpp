#include <iostream>
#include <string>
using namespace std;

// objects are like entities in real world
// classes are the blue print of this entities
// Encapsulation is the wrapping up of data and member function in to single unit called class
// Abstraction
// inheritance
// polymorphism

class Student
{
    // public:
    // data and methods are accessble to every one
    // private:
    // data and methods are accessble only in the class
    // protected:
    // data and methods are accessble only from class and it's derived class

private:
    string password; // this is data hiding of encapsulation

public:
    // attributes or properties
    string name;
    int rollNo;
    int marks;

    // methods or memberFunction
    void changeName(string newName)
    {
        name = newName;
    }

    // setter
    void addPassword(string passw)
    {
        password = passw;
    }

    // getter
    string showPassword()
    {
        return password;
    }
};

int main()
{
    Student s1;
    
    // cout<<"enter name, roolNo, marks of the student :";
    // cin>>s1.name>>s1.rollNo>>s1.marks;
    // cout<<"enter new name for student :";
    // string newName;
    // cin>>newName;
    // s1.changeName(newName);
    // cout<<s1.name<<endl<<s1.rollNo<<endl<<s1.marks;

    s1.addPassword("abc123");
    cout << s1.showPassword();

    return 0;
}