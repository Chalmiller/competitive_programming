#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>

using namespace std;

int vectors() {

    // Dynamic Arrays == Vectors
    vector<int> v;

    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    cout << v[0] << "\n";

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << "\n";
    }

    for (auto x : v) {
        cout << x << "\n";
    }

    cout << v.back() << "\n";
    v.pop_back();

    vector<int> v2(10, 5);
    for (auto x : v2) {
        cout << x << "\n";
    }

    // Strings

    string a = "hatti";
    string b = a+a;
    cout << b << "\n";
    b[5] = 'v';
    cout << b << "\n";
    string c = b.substr(3,4);
    cout << c << "\n";

    // Set

    set<int> s;
    s.insert(3);
    s.insert(4);
    s.insert(5);
    cout << s.count(3) << "\n";
    cout << s.count(4) << "\n";

    s.erase(3);
    s.insert(4);
    cout << s.count(3) << "\n";
    cout << s.count(4) << "\n";

    set<int> s2 = {2,5,6,8};
    cout << s.size() << "\n";
    for (auto x : s) {
        cout << x << "\n";
    }
    // automatically generate an iterator of the smallest value within the set
    auto it = s2.begin();
    // to print the element to which the iterator points
    cout << *it << "\n";

    // iterate through a set with an iterator
    for  (auto it = s2.begin(); it != s2.end(); it++) {
        cout << *it << "\n";
    }

    multiset<int> s3;
    s3.insert(5);
    s3.insert(5);
    s3.insert(5);
    cout << s.count(5) << "\n";
    // to earse one instance in a multiset use
    s3.erase(s3.find(5));

    // Maps
    map<string, int> m;
    m["monkey"] = 4;
    m["banana"] = 3;
    m["harpsichord"] = 9;
    cout << m["banana"] << "\n";

    // Check if a key exists in map
    if (m.count("banana")) {
        // key exists
    }

    for (auto x : m) {
        cout << x.first << " " << x.second << "\n";
    }

    // bitset array
    bitset<10> b;
    b[1] = 1;
    b[3] = 1;
    b[4] = 1;
    b[7] = 1;

    // or instantiate a bitset using the following method
    bitset<10> b2(string("0010011010"));
 }

int main() {
    int z;
    z = vectors();
    cout << "main output" << z << "\n"; 

    return 0;
}

