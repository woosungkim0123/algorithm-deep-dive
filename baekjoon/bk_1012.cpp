#include <bits/stdc++.h>
using namespace std;

const int max_n = 51;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int a[max_n][max_n];
int visited[max_n][max_n];
int m, n, k, y, x, ret, ny, nx, t;
void dfs(int y, int x) {
	visited[y][x] = 1;
	for(int i = 0; i < 4; i++) {
		ny = dy[i] + y;
		nx = dx[i] + x;
		if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
		if( a[ny][nx] == 1 && !visited[ny][nx] == 1) {
			dfs(ny, nx);
		}
	
	}
	return;
}

int main() {
	cin >> t;
	while(t--) {
		fill(&a[0][0], &a[0][0] + 51 * 51, 0);
		fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
		cin >> m >> n >> k;
		ret = 0;
		
		for (int i = 0; i < k; i++) {
			cin >> x >> y;
			a[y][x] = 1;
		}
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(a[i][j] == 1 && !visited[i][j]) {
					dfs(i, j);
					ret++;
				} 
				
			}
		} 
		cout << ret << "\n";
	}

}
