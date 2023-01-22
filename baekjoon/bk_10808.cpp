#include <bits/stdc++.h>
using namespace std;

string str;
// int asc = 97;
int cnt[26];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> str;
	for(char a : str) {
		cnt[a - 'a']++;
	}
	/*
	for(int i = 0; i < str.size(); i++) {
		char c = str[i];
    	int n = int(c) - asc;
    	cnt[n] += 1;

	}
	*/
	for(int i =0; i < 26; i++) cout << cnt[i] << " ";
	return 0;
}
