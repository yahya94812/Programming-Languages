// Set, Unique Sorted Elements
#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> s;

    s.insert(10); // Insert element - O(log n)
    s.erase(10);  // Remove element - O(log n)
    s.find(10);   // Find element - O(log n)
    s.count(10);  // Check if exists (returns 0 or 1) - O(log n)
    s.size();     // Get size - O(1)
    s.empty();    // Check if empty - O(1)

    // Iteration (elements are sorted)
    for (auto x : s)
        cout << x << " ";

    // Multiset allows duplicates
    multiset<int> ms;
    ms.insert(10);
    ms.insert(10); // Both elements will be stored

    // Use cases: Remove duplicates, maintain sorted order
    
    return 0;
}
