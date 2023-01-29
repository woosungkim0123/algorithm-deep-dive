#include <bits/stdc++.h>
using namespace std;


string s, ret;
int cnt[200], flag;
char mid;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> s;
	
	for(char a : s) cnt[a]++; // 문자가 몇개 있나가 중요해서 카운팅 배열을 만들었다 
	
	for(int i = 'Z'; i >= 'A'; i--) { // 오름차순 때문에 Z부터 붙였다. 
		if(cnt[i]) {
			if(cnt[i] & 1){ // 홀수인가? 
				mid = char(i);
				flag++;
				cnt[i]--; 
			}
			if(flag == 2) break;
			for(int j = 0; j < cnt[i]; j += 2) {
				ret = char(i) + ret;
				ret += char(i);
			}
		}
	}
	if(mid) ret.insert(ret.begin() + ret.size() / 2, mid);
	if(flag == 2) cout << "I'm Sorry Hansoo" << "\n";	
	else cout << ret << "\n";
} 
