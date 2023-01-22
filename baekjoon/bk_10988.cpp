#include<bits/stdc++.h>
using namespace std;

vector<int> v;
string s;
int ret = 1;
int main () {
	cin >> s;
	for(int i =0 ; i <s.size(); i++) {
		v.push_back((int) s[i]);
	}
	for(int i = 0; i < s.size(); i++) {
		if(v[i] == (int) s[s.size() - i - 1]) continue;
		ret = 0;
		break;
	}
	cout << ret << "\n";
	return 0;
}
