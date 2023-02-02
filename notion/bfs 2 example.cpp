#include <bits/stdc++.h>
using namespace std;
const int max_n = 104;
int n, m, sy, sx, ey, ex, ny, nx, x, y;
int visited[max_n][max_n];
int a[max_n][max_n];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int main() {
	cin >> n >> m;
	cin >> sy >> sx;
	cin >> ey >> ex;
	
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}
	queue<pair<int, int>> q;
	visited[sy][sx] = 1;
	q.push({sy, sx});
	while(q.size()){
		tie(y, x) = q.front();
		q.pop();
		for(int i = 0; i < 4; i++) {
			ny = y + dy[i];
			nx = x + dx[i];
			if(ny < 0 || ny >= n || nx < 0 || nx >= m || a[ny][nx] == 0) continue;
			if(visited[ny][nx]) continue;
			visited[ny][nx] = visited[y][x] + 1;
			q.push({ny, nx});
		}
	}
	cout << visited[ex][ey] << "\n";
}
