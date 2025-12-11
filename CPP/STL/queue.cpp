#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int> q;

    q.push(10);
    cout<<q.front()<<endl;
    cout<<q.back()<<endl;
    cout<<q.size()<<endl;
    cout<<q.empty()<<endl;
    q.pop();
    
    return 0;
}