#include<bits/stdc++.h>
using namespace std;


const int INF = 987654321;

char a[1004][1004];
int fire_check[1004][1004], person_check[1004][1004];
int n, m, y, x, sy, sx, ret, dy[4] = {-1, 0, 1, 0}, dx[4] = {0, 1, 0, -1};

bool in(int a, int b) {
	return 0 <= a && a < n && 0 <= b && b < m;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL); 
	cin >> n >> m;
	queue<pair<int, int>>q;
	fill(&fire_check[0][0], &fire_check[0][0] + 1004 * 1004, INF);
	// INF를 안하게되면 불이 아무것도 없을때 FIRE_CHECK가 0으로 정의가됨
	// 불이 아무것도 없다는 반례가있음. 그래서 그 부분때문에 INF사용 
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin >> a[i][j];
			if(a[i][j] == 'F') {
				fire_check[i][j] = 1; // 불은 여러개 (문제를 잘 읽어야함 주의) 
				q.push({i, j});
			} else if(a[i][j] == 'J') {
				sy = i; sx = j;
			}
		}
	}
	
	while(q.size()) {
		tie(y, x) = q.front();
		q.pop();
		for(int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if(!in(ny, nx)) continue;
			if(fire_check[ny][nx] != INF || a[ny][nx] == '#') continue;
			fire_check[ny][nx] = fire_check[y][x] + 1;
			q.push({ny, nx});
		} 
		
	}
	person_check[sy][sx] = 1;
	q.push({sy, sx});
	
	while(q.size()) {
		tie(y, x) = q.front();
		q.pop();
		if(x == m - 1 || y == n - 1 || x == 0 || y == 0) { // 가장 자리에 도착하면 빠져나옴 
			ret = person_check[y][x];
			break;
		}
		
		for(int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if(!in(ny, nx)) continue;
			if(person_check[ny][nx] || a[ny][nx] == '#') continue;
			if(fire_check[ny][nx] <= person_check[y][x] + 1) continue;
			person_check[ny][nx] = person_check[y][x] + 1;
			q.push({ny, nx});
		} 	
	}
	
	if(ret != 0) cout << ret << "\n";
	else cout << "IMPOSSIBLE" << "\n";
	return 0;
}
/*
	불의 최단거리와 사람의 최단거리를 비교하면되지않을까? 가중치 같음 -> bfs
	불 최단 거리 만들고  visited 배열로 만들어놓고 
	사람의 최단거리를 구할때 if문으로 불의 최단거리를 비교해서 빠르면 전진가능하게 
*/
