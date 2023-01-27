#include <bits/stdc++.h>
using namespace std;

/*
// first solution

int a[26];
int c;
vector<int> v;

int main () {
	cin >> c;
	for(int i =0; i < c; i++) {
		string s; int sc;
		cin >> s;
		sc = (int) s[0] - 97;
		a[sc]++;	
	}
	for(int i = 0; i < 26; i++) {
		if(a[i] < 5) continue;
		v.push_back(i + 97);
	}
	
	if(v.size() == 0){
		cout << "PREDAJA" << "\n";
	} else {
		for(int i = 0; i < v.size(); i++) {
			cout << (char) v[i]  << "";
		}
	}
	return 0;
}
*/

int n, cnt[26];
string s, ret;

int main() {
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> s;
		cnt[s[0] - 'a']++; // 배열은 integar 기반의 index를 사용하기 때문에 c++에서 자동으로 int화 시켜줌 
	}
	
	for(int i = 0; i < 26; i++) if(cnt[i] >= 5) ret += (i + 'a'); // char(i + 'a') 이런식으로 문자화 시켜줘야하지만 숫자도 문자화되서 들어가게됨 
	if(ret.size()) cout << ret << "\n";
    else cout << "PREDAJA" << "\n"; 
	
}
