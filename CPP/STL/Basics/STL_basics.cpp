// The Standard Template Library (STL) is a set of C++ template classes and functions that provide common data structures and algorithms.

// STL is divided into 4 main components:
// Containers: Store collections of objects e.g., vector, list, set, map
// Algorithms: Procedures that operate on containers e.g., sort(), find(), count()
// Iterators: Objects for traversing containers	begin(), end(), ++it
// Functors: Function objects used with algorithms e.g.,std::greater, custom comparators

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
    // 1.Containers (Data structures)
    // Containers hold data. There are different types depending on your need:

    // Sequence Containers (linear)
    // vector  dynamic array
    // deque  double-ended queue
    // list  doubly linked list

    // Associative Containers (sorted by key)
    // set  unique elements, sorted
    // map  key-value pairs, unique keys
    // multiset / multimap  allow duplicates

    // Unordered Containers (hash-based, fast lookup)
    // unordered_set
    // unordered_map


    // 2.Algorithms
    // stl provide many generic algorithms
    vector<int> v = {1, 3, 5, 7, 2};

    sort(v.begin(), v.end()); // v.begin() method return the pointer to the first element

    reverse(v.begin(), v.end());

    for (auto x : v)
        cout << x << " ";
    cout << endl;

    auto it = find(v.begin(), v.end(), 3); // std::find returns an iterator to the first occurrence of 3, or v.end() if not found.
    cout << *it << endl;


    // 3.Iterators
    // Iterators behave like pointers. They allow algorithms to work with containers
    vector<int>::iterator it1 = v.begin();
    while (it1 != v.end())
    {
        cout << *it1 << " ";
        it1++;
    }
    // STL uses iterators instead of indices for container independence


    // 4.Functors (Function Objects)
    // Objects that behave like functions. Can be passed to algorithms
    sort(v.begin(), v.end(), greater<int>()); //sort in descending order


    return 0;
}
