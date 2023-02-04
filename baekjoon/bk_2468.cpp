/*
	https://www.acmicpc.net/problem/2468
*/

#include <bits/stdc++.h>
using namespace std;

int a[101][101], visited[101][101], n, temp, ret = 1;
int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, 1, 0, -1 };

void dfs(int y, int x, int d) {
	visited[y][x] = 1;
	for(int i = 0; i < 4; i++) {
		int ny = dy[i] + y;
		int nx = dx[i] + x;
		
		if(ny < 0 || ny >= n || nx < 0 || nx >= n ) continue;
		if(!visited[ny][nx] && a[ny][nx] > d) {
			dfs(ny, nx, d);	
		}

	
	}
	return;
}

int main() {
	cin >> n;
	for(int i = 0; i< n; i++) {
		for(int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}
	for(int d = 1; d <= 101; d++) {
		fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
		int cnt = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(a[i][j] > d && !visited[i][j]) {
					dfs(i, j, d);
					cnt += 1;
				}
			}
		}
		
		ret = max(ret, cnt);
	}
	cout << ret << "\n";
	return 0;
}
