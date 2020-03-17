#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>


using namespace std;

void search(int k) {
    if (k == n) {
        // process subset
    } else {
        search(k+1);
        subset.push_back(k);
        search(k+1);
        subset.pop_back();
    }
}

int main() {
    return 0;
}