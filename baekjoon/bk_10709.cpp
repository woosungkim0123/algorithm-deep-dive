#include <bits/stdc++.h>

using namespace std;

int h, w;
string s;

int a[104][104];

void dfs(int y, int x) {
	int dx = x + 1;
	if(dx < w && a[y][dx] != 0) {
		a[y][dx] = a[y][x] + 1;
		dfs(y, dx);
	}
	
}

int main()
{
	cin >> h >> w;

	for (int i = 0; i < h; i++) {
		cin >> s;
		for(int j = 0; j < w; j++) {
			if(s[j] == '.') {
				a[i][j] = -1;
			} 
		} 
	}
	for(int i = 0; i < h; i++) {
		for(int j = 0; j < w; j++) {
			if(a[i][j] == 0) {
				dfs(i, j);
			}
		}
	}
	
	for(int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			cout << a[i][j] << " ";
		}
		cout << "\n";
	}


	return 0;
}
