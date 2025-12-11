# STL for DSA and Competitive Programming

## 1. Vector - Dynamic Arrays

The most commonly used container in competitive programming.

```cpp
#include <vector>
using namespace std;

// Declaration and initialization
vector<int> v;                    // Empty vector
vector<int> v(5);                 // Size 5, default values (0)
vector<int> v(5, 10);            // Size 5, all elements = 10
vector<int> v = {1, 2, 3, 4, 5}; // Initialize with values

// Common operations
v.push_back(6);        // Add element at end - O(1)
v.pop_back();          // Remove last element - O(1)
v.size();              // Get size - O(1)
v.empty();             // Check if empty - O(1)
v.clear();             // Remove all elements - O(n)
v[i];                  // Access element at index i - O(1)
v.front();             // First element - O(1)
v.back();              // Last element - O(1)

// Iteration
for(int i = 0; i < v.size(); i++) cout << v[i] << " ";
for(auto x : v) cout << x << " ";  // Range-based for loop
```

## 2. String - Text Processing

```cpp
#include <string>

string s = "hello";
s += "world";          // Concatenation
s.length();            // Get length
s.substr(1, 3);        // Substring from index 1, length 3
s.find("ell");         // Find substring (returns position or string::npos)
s.push_back('!');      // Add character at end
s.pop_back();          // Remove last character

// String to number and vice versa
int num = stoi("123");           // String to int
string str = to_string(123);     // Int to string
```

## 3. Stack - LIFO Operations

```cpp
#include <stack>

stack<int> st;
st.push(10);           // Add element - O(1)
st.pop();              // Remove top element - O(1)
st.top();              // Access top element - O(1)
st.empty();            // Check if empty - O(1)
st.size();             // Get size - O(1)

// Use cases: Expression evaluation, DFS, matching brackets
```

## 4. Queue - FIFO Operations

```cpp
#include <queue>

queue<int> q;
q.push(10);            // Add element at rear - O(1)
q.pop();               // Remove front element - O(1)
q.front();             // Access front element - O(1)
q.back();              // Access rear element - O(1)
q.empty();             // Check if empty - O(1)
q.size();              // Get size - O(1)

// Use cases: BFS, level order traversal
```

## 5. Priority Queue - Heap Operations

```cpp
#include <queue>

// Max heap (default)
priority_queue<int> pq;
pq.push(10);           // Insert element - O(log n)
pq.pop();              // Remove top element - O(log n)
pq.top();              // Access top element - O(1)

// Min heap
priority_queue<int, vector<int>, greater<int>> minpq;

// Custom comparator for pairs (sort by second element)
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

// Use cases: Dijkstra's algorithm, finding kth largest/smallest
```

## 6. Set - Unique Sorted Elements

```cpp
#include <set>

set<int> s;
s.insert(10);          // Insert element - O(log n)
s.erase(10);           // Remove element - O(log n)
s.find(10);            // Find element - O(log n)
s.count(10);           // Check if exists (returns 0 or 1) - O(log n)
s.size();              // Get size - O(1)
s.empty();             // Check if empty - O(1)

// Iteration (elements are sorted)
for(auto x : s) cout << x << " ";

// Multiset allows duplicates
multiset<int> ms;
ms.insert(10);
ms.insert(10);         // Both elements will be stored

// Use cases: Remove duplicates, maintain sorted order
```

## 7. Map - Key-Value Pairs

```cpp
#include <map>

map<string, int> m;
m["apple"] = 5;        // Insert/update - O(log n)
m.insert({"banana", 3}); // Alternative insert
m.erase("apple");      // Remove by key - O(log n)
m.find("apple");       // Find by key - O(log n)
m.count("apple");      // Check if key exists - O(log n)
m.size();              // Get size - O(1)

// Iteration (keys are sorted)
for(auto p : m) {
    cout << p.first << ": " << p.second << "\n";
}

// Unordered map for O(1) average operations
#include <unordered_map>
unordered_map<string, int> um;

// Use cases: Frequency counting, memoization
```

## 8. Algorithms - Essential Functions

```cpp
#include <algorithm>

vector<int> v = {3, 1, 4, 1, 5};

// Sorting
sort(v.begin(), v.end());                    // Ascending order
sort(v.begin(), v.end(), greater<int>());    // Descending order

// Binary search (on sorted array)
binary_search(v.begin(), v.end(), 3);        // Returns true/false
lower_bound(v.begin(), v.end(), 3);          // Iterator to first >= 3
upper_bound(v.begin(), v.end(), 3);          // Iterator to first > 3

// Min/Max
*min_element(v.begin(), v.end());            // Minimum element
*max_element(v.begin(), v.end());            // Maximum element
min(a, b);                                   // Minimum of two values
max(a, b);                                   // Maximum of two values

// Reverse
reverse(v.begin(), v.end());

// Next/Previous permutation
next_permutation(v.begin(), v.end());
prev_permutation(v.begin(), v.end());

// Count occurrences
count(v.begin(), v.end(), 1);                // Count of element 1

// Remove duplicates (after sorting)
v.erase(unique(v.begin(), v.end()), v.end());
```

## 9. Pair and Tuple

```cpp
#include <utility>  // for pair
#include <tuple>    // for tuple

// Pair
pair<int, int> p = {3, 4};
pair<int, int> p = make_pair(3, 4);
cout << p.first << " " << p.second;

// Sorting pairs (sorts by first, then by second)
vector<pair<int, int>> vp = {{3, 4}, {1, 2}, {3, 1}};
sort(vp.begin(), vp.end());

// Tuple
tuple<int, int, string> t = make_tuple(1, 2, "hello");
get<0>(t);  // Access first element
get<1>(t);  // Access second element
get<2>(t);  // Access third element
```

## 10. Deque - Double-ended Queue

```cpp
#include <deque>

deque<int> dq;
dq.push_back(1);       // Add at end - O(1)
dq.push_front(2);      // Add at front - O(1)
dq.pop_back();         // Remove from end - O(1)
dq.pop_front();        // Remove from front - O(1)
dq.front();            // Access first element - O(1)
dq.back();             // Access last element - O(1)

// Use cases: Sliding window problems, implementing queue with both ends
```

## Common Competitive Programming Patterns

### 1. Frequency Counting
```cpp
map<int, int> freq;
for(int x : arr) {
    freq[x]++;
}
```

### 2. Two Pointers with Set
```cpp
set<int> s;
for(int i = 0; i < n; i++) {
    if(s.count(target - arr[i])) {
        // Found pair
    }
    s.insert(arr[i]);
}
```

### 3. Sliding Window Maximum
```cpp
deque<int> dq;  // Store indices
priority_queue<pair<int, int>> pq;  // Store {value, index}
```

### 4. Custom Sorting
```cpp
// Sort by second element of pair
sort(v.begin(), v.end(), [](pair<int,int> a, pair<int,int> b) {
    return a.second < b.second;
});

// Sort array indices by their values
vector<int> indices(n);
iota(indices.begin(), indices.end(), 0);  // Fill with 0, 1, 2, ...
sort(indices.begin(), indices.end(), [&](int i, int j) {
    return arr[i] < arr[j];
});
```

## Time Complexities Summary

| Container | Insert | Delete | Search | Access |
|-----------|---------|---------|---------|---------|
| Vector | O(1) amortized | O(n) | O(n) | O(1) |
| Stack/Queue | O(1) | O(1) | - | O(1) top/front |
| Priority Queue | O(log n) | O(log n) | - | O(1) top |
| Set/Map | O(log n) | O(log n) | O(log n) | - |
| Unordered Set/Map | O(1) avg | O(1) avg | O(1) avg | - |

## Pro Tips for Competitive Programming

1. **Always use `ios_base::sync_with_stdio(false); cin.tie(NULL);`** for faster I/O
2. **Use `auto`** to avoid typing long type names
3. **Use range-based for loops** when you don't need indices
4. **Prefer `unordered_map/unordered_set`** when order doesn't matter
5. **Use `vector.reserve()`** if you know the approximate size
6. **Remember that `map/set` are sorted**, `unordered_map/unordered_set` are not
7. **Use `pair` and `tuple`** for multiple return values
8. **Master binary search functions**: `lower_bound`, `upper_bound`, `binary_search`