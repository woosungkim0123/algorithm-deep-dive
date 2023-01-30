/*
	https://www.acmicpc.net/problem/3986
*/

#include <bits/stdc++.h>
using namespace std;

int n, ret;
string s;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n;
	
	while(n--) {
		cin >> s;
		stack<char> stk;
	
		for(char a : s) {
			if(stk.size() && stk.top() == a) stk.pop();
			else stk.push(a);
		}
		if(stk.size() == 0) ret++;
	}
	
	cout << ret << "\n";
	return 0; 
}
