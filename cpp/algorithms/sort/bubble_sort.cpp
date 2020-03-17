#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

int main() {

    return 0;
}

int bubble_sort(int array []) {
    int n = array.size();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-1; j++) {
            if (array[j] > array[j+1]) {
                swap(array[j], array[j+1]);
            }
        }
    }
}

int binary_search() {
    int a = 0, b = n-1;
    while(a<= b) {
        int k = (a+b)/2;
        if (array[k] == x) {

        }
        if (array[k] > x) b = k-1;
        else a = k+1;
    }
}