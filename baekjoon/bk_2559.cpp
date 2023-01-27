#include <bits/stdc++.h>
using namespace std;

int n, k;
int sum;
int temp, psum[100001];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n >> k;
	
	for (int i = 1; i <= n; i++) {
		cin >> temp;
		psum[i] = temp;
	}
	for (int i = 0; i <= n; i++) {
		cout << psum[i] << "\n";
	}

	
}
