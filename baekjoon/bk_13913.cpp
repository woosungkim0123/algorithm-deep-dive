#include <bits/stdc++.h>

using namespace std;
#define prev aaa
#define next aaaa

const int MAX = 200004;

int n, k, ret;

int visited[MAX];
int prev[MAX];
vector<int> v;
int main()
{
	cin >> n >> k;
	
	visited[n] = 1;
	
	queue<int> q;
	q.push(n);

	while(q.size()){
		int now = q.front();
		q.pop();
		if(now == k) {
			ret = visited[k];
			break;
		}
	
		for(int next : {now -1, now + 1, now * 2}) {
			if(next >= MAX || next < 0 || visited[next]) continue;
        	q.push(next);
            visited[next] = visited[now] + 1;
            prev[next] = now;	
		}
		
	}
	for(int i = k; i != n; i = prev[i]) {
		v.push_back(i);
	}
	v.push_back(n);
	reverse(v.begin(), v.end());
	cout << ret - 1 << "\n";
	
	for(int i : v) {
		cout << i << ' ';
	}
	return 0;
} 

