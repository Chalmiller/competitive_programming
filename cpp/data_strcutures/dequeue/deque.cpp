#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <deque>

using namespace std;

int deque_method() {
    deque<int> d;
    d.push_back(5);
    d.push_back(2);
    d.push_front(3);
    d.pop_back();
    d.pop_front();
}

int main() {
    return 0;
}