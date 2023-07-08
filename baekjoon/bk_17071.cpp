#include <bits/stdc++.h>

using namespace std;

const int max_n = 500000;

int n, k, ret, ok, turn =1;
int visited[2][max_n + 4];


int main()
{
	cin >> n >> k;
	if(n == k) {
		cout << 0 << "\n";
		return 0;
	} 
	queue<int> q;
	visited[0][n] = 1;
	q.push(n);

	while(q.size()){
		k += turn;
		if(k > max_n) {
			break;
		}
		if(visited[turn % 2][k]) {
			ok = true;
			break;
		}
		int q_size = q.size();
		for (int i = 0; i < q_size; i++) {
			int x = q.front();
			q.pop();
			
			for(int nx : {x -1, x + 1, x * 2}) {
				if(nx > max_n || nx < 0 || visited[turn % 2][nx]) {
					continue;
				}
				visited[turn % 2][nx] = visited[(turn + 1) % 2][x] + 1;
				if(nx == k) {
					ok = 1; 
					break;
				}
				q.push(nx);
			}
			if(ok) {
				break;
			}
		}
		if(ok) {
			break;
		}
		turn++;
	}
	if(ok) cout << turn << "\n";
	else cout << -1 << "\n";
	
	return 0;
} 

