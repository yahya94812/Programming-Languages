// Algorithms, Essential functions
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> v = {3, 1, 4, 1, 5};

    // sorting
    sort(v.begin(), v.end());
    sort(v.begin(), v.end(), greater<int>()); // Descending order

    // binary search (on sorted array)
    binary_search(v.begin(), v.end(), 3); // return true/false
    lower_bound(v.begin(), v.end(), 3);
    // lower_bound(begin, end, value); work with only sorted containers
    // Returns an iterator to the first element ≥ value.
    // If value is not found, returns the first element greater than value.
    upper_bound(v.begin(), v.end(), 3);
    // Returns an iterator to the first element > value

    // Min/Max
    cout << "minimum value: " << *min_element(v.begin(), v.end()) << endl;
    cout << "maximum value by dereferencing iterator: " << *max_element(v.begin(), v.end());
    // min(a, b);
    // max(a, b);

    // Reverse
    reverse(v.begin(), v.end());

    // Next/Previous permutation
    next_permutation(v.begin(), v.end());
    prev_permutation(v.begin(), v.end());

    // count occurrences
    count(v.begin(), v.end(), 1); // count of element 1

    // remove duplicates (after sorting)
    v.erase(unique(v.begin(), v.end()), v.end());

    return 0;
}