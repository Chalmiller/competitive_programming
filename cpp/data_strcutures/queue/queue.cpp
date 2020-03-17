#include <iostream>
#include <queue>

using namespace std;

int queue_method() {
    queue<int> q;
    q.push(3);
    q.push(2);
    q.push(5);

    cout << q.front();
    q.pop();
    cout << q.front();
}

int main() {
    return 0;
}