#include<bits/stdc++.h>
using namespace std;

int n, w, h;
char a[1004][1004];
string s; 

int main() {
	cin >> n;
	
	while(n--) {
		cin >> w >> h;
		for(int i = 0; i < h; i++) {
			cin >> s;
			for(int j = 0; j < w; j++) {
				a[i][j] = s[j];
			}
		}
	}
	for(int i = 0; i < h; i++) {
		for(int j = 0; j < w; j++) {
			cout << a[i][j] << " ";
		}
		cout << "\n";
	}
}
