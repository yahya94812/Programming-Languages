// Map, Key-Value Pairs
#include <iostream>
#include <map>
#include <unordered_map>
using namespace std;

int main()
{
    map<string, int> m;
    m["apple"] = 5;          // Insert/update - O(log n)
    m.insert({"banana", 3}); // Alternative insert
    m.erase("apple");        // Remove by key - O(log n)
    m.find("apple");         // Find by key - O(log n)
    m.count("apple");        // Check if key exists - O(log n)
    m.size();                // Get size - O(1)
    // Iteration (keys are sorted)
    for (auto p : m)
    {
        cout << p.first << ": " << p.second << "\n";
    }

    // Unordered map for O(1) average operations
    unordered_map<string, int> um;

    // Use cases: Frequency counting, memoization

    return 0;
}