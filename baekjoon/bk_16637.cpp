#include <bits/stdc++.h>

using namespace std;

int n, ret = -987654321;
string str;

vector<int> num;
vector<char> oper_str;



int oper(char a, int b, int c) 
{
	if(a == '+') return b + c;
	if(a == '-') return b - c;
	if(a == '*') return b * c;
}

/*
 3 x 8 + 5 는
 24 + 5랑
 3 x 13의 
 두가지 결과가 있음 
*/
void go(int idx, int _num)
{
	if (idx == num.size() - 1) {
		ret = max(ret, _num);
		return;
	}
	
	go(idx + 1, oper(oper_str[idx], _num, num[idx + 1]));
	if(idx + 2 <= num.size() - 1) {
		int temp = oper(oper_str[idx + 1], num[idx + 1], num[idx + 2]);
		go(idx + 2, oper(oper_str[idx], _num, temp));
	}
	return;
	
}




int main()
{
	cin >> n >> str;
	
	for (int i = 0; i < n; i++) {
		if(i % 2 == 0) {
			num.push_back(str[i] - '0');
		} else {
			oper_str.push_back(str[i]);
		}
	}
	go(0, num[0]);
	cout << ret << "\n";

	
}
