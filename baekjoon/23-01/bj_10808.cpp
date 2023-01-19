#include <bits/stdc++.h>
using namespace std;

string w;
int asc = 97;
int arr[26];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> w;
	for(int i = 0; i < w.size(); i++) {
		char c = w[i];
    	int n = int(c) - asc;
    	arr[n] += 1;

	}
	
	for(int i =0; i < 26; i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
