#include <bits/stdc++.h>
using namespace std;

int a[4];
int arr[104];
int sum;

int main () {
	cin >> a[1] >> a[2] >> a[3];
	for (int i = 0 ; i < 3; i++) {
		int s, e;
		cin >> s >> e;
		for(int j = s; j < e; j++) {
			arr[j]++;
		}
	}
	for(int i = 1; i < 100; i++) {
		if(arr[i] == 0) continue;
		sum+= a[arr[i]] * arr[i];
	}
	cout << sum << "\n";
	return 0;
}
