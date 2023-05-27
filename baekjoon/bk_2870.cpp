#include <bits/stdc++.h>

using namespace std;

int n;
vector<string> v;
string ret, s;

bool cmp(string a, string b)
{
	if(a.size() == b.size()) {
		return a < b;
	}
	return a.size() < b.size();
}

int main()
{
	cin >> n;
	
	while(n--) {
		cin >> s;
		
		ret = "";
		for (int i = 0; i < s.size(); i++) {	
			if (s[i] < 65) {
				if (ret == "0") {
					ret = "";
				}
				ret += s[i];
			} 
			if (ret != "" && (s[i] >= 65 || i == s.size() - 1)) {
				v.push_back(ret);
				ret = "";
			}
		}
	}
	sort(v.begin(), v.end(), cmp);
	
	for (string i : v) {
		cout << i << "\n";
	}

	return 0;
}
