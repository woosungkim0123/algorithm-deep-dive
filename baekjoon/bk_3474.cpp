#include <bits/stdc++.h>

using namespace std;

int t, n;

int a[104][104];


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		cin >> n;
		
		int ret2 = 0;
		int ret5 = 0;
		
		for (int j = 2; j <= n; j *= 2) {
			ret2 += n / j;
		}
		
		for (int j = 5; j <= n; j *= 5) {
			ret5 += n / j;
		}

		cout << min(ret2, ret5) << "\n";
	}

	return 0;
}
