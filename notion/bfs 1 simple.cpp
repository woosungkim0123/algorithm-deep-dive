#include <bits/stdc++.h>
using namespace std;
vector<int> adj[100];
int visited[100];
int nodeList[] = { 10, 12, 14, 16, 18, 20, 22, 24};

void bfs(int here) {
	queue<int> q;
	visited[here] = 1;
	q.push(here);
	while(q.size()){
		int here= q.front();
		q.pop();
		
		for(int there : adj[here]) {
			if(visited[there]) continue;
			visited[there] = visited[here] + 1;
			q.push(there);
		}
	}
}

int main() {
	adj[10].push_back(12);
	adj[10].push_back(14);
	adj[10].push_back(16);
	
	adj[12].push_back(18);
    adj[12].push_back(20);

    adj[20].push_back(22);
    adj[20].push_back(24);

	bfs(10);
}
