#include<bits/stdc++.h>
using namespace std;

/* 
// - first solution 

vector<int> v;
string s;
int ret = 1;
int main () {
	cin >> s;
	for(int i =0 ; i < s.size(); i++) {
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
*/

string s, temp;

int main() {
	cin >> s;
	temp = s;
	
	reverse(temp.begin(), temp.end());
	if(temp == s) cout << 1 << "\n";
	else cout << 0 << "\n";
}
