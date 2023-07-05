#include <bits/stdc++.h>

using namespace std;


int n, k;
const int MAX = 100000;
int visited[100004];
long long cnt[100004];

int main()
{
	cin >> n >> k;
	
	if(n == k) {
		puts("0"); 
		puts("1");
	}
	
	visited[n] = 1;
	cnt[n] = 1;
	
	queue<int> q;
	q.push(n);
	
	while(!q.empty()) {
		int now = q.front();
		q.pop();
		
		for (int next : {now - 1, now + 1, now * 2}) {
			if(0 <= next && next <= MAX) {
				if(!visited[next]) {
					q.push(next);
					visited[next] = visited[now] + 1;
					cnt[next] += cnt[now];
				} else if(visited[next] == visited[now] + 1) {
					cnt[next] += cnt[now];
				}
			}
		}
		
	}
	
	cout << visited[k] - 1 << "\n";
	cout << cnt[k] << "\n"; 
}


