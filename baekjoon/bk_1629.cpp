#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a, b, c;

ll go(ll a, ll b) {
	if(b == 1) return a % c;
	ll ret = go(a, b / 2);
	ret = (ret * ret) % c;
	if(b % 2) ret = (ret * a) % c;// 1�� ���ͼ� true, Ȧ����� �ѹ��� ��������� 
	return ret;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> a >> b >> c;
	
	long long result = 1;
	cout << go(a, b) << "\n";
}
