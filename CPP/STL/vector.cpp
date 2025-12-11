// vector: dynamic arrays, it is a type container in STL
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // vector<int> v; //empty vector
    // vector<int> v(5); //size=5, default values=0
    // vector<int> v(5, 10); //size=5, default values=10
    vector<int> v = {1, 2, 3, 4, 5};

    v.push_back(6); //O(1)
    v.pop_back(); //O(1)
    cout<<v.size()<<endl; //O(1)
    cout<<v.empty()<<endl; //check if empty, O(1)
    int i = 0;
    cout<<v[i]<<endl; //O(1)
    cout<<v.front()<<endl; //first element, O(1)
    cout<<v.back()<<endl; //last element, O(1)

    for(int i=0; i<v.size(); i++) cout<<v[i]<<" ";
    cout<<endl;
    for(auto x : v) cout<<x<<" ";
    cout<<endl;
   
    v.clear(); //O(n)

    for(int x : v) cout<<x<<" "; //it is similar to above line so use auto to avoid writing long datatypes
    cout<<endl;
    
    return 0;
}