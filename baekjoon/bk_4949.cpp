/*
	https://www.acmicpc.net/problem/4949
*/
#include <bits/stdc++.h>

using namespace std;

bool check(string s)
{
    stack<int> stk;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ')') {
            if(stk.size() == 0 || stk.top() == '[') {
                return false;
            }
            else {
                stk.pop();
            }
        }
        else if (s[i] == ']') {
            if(stk.size() == 0 || stk.top() == '(') {
                return false;
            }
            else {
                stk.pop();
            }
        }
        else if(s[i] == '(' || s[i] == '[') {
            stk.push(s[i]);
        }
    } 
    return !stk.size();
}

int main()
{
    while(true) {
        string s;
        getline(cin, s);
        
        if (s == ".") {
            break;    
        }
        
		if (check(s)) {
            cout << "yes\n";
        }
        else {
            cout << "no\n";
        }
    }
    return 0;
}
