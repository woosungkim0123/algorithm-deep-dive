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
		cnt[s[0] - 'a']++; // �迭�� integar ����� index�� ����ϱ� ������ c++���� �ڵ����� intȭ ������ 
	}
	
	for(int i = 0; i < 26; i++) if(cnt[i] >= 5) ret += (i + 'a'); // char(i + 'a') �̷������� ����ȭ ������������� ���ڵ� ����ȭ�Ǽ� ���Ե� 
	if(ret.size()) cout << ret << "\n";
    else cout << "PREDAJA" << "\n"; 
	
}
