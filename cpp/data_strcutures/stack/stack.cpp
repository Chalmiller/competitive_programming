#include <iostream>
#include <stack>

using namespace std;

int stack_method() {
    stack<int> s;
    s.push(3);
    s.push(2);
    s.push(5);

    cout << s.top();
    
    s.pop();

    cout << s.top();

}

int main() {
    return 0;
}