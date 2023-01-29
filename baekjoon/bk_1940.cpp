#include <bits/stdc++.h>
using namespace std;

int n, m;
int a[15001], cnt;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	
	for(int i = 0; i < n; i++) cin >> a[i];
	
	if(m > 200000) cout << 0 << "\n"; // 이게 중요 10만 두개를 더하는 것이니 20만을 넘어설 수가 없음. 해야 맞는 경우가 있고 안하면 틀리는 경우도 있음 
	else {
		for(int i = 0; i < n; i++) {
			for(int j = i + 1; j < n; j++) {
				if(a[i] + a[j] == m) cnt++;
			}
		}
		cout << cnt << "\n";
	}
	
	return 0;
}
