/*
	https://www.acmicpc.net/problem/1159
*/
#include <bits/stdc++.h>
using namespace std;

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
	
	return 0;
}
