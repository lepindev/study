/***
/*
    description: A

    author:    lepindev
    created:   08.03.2023 23:07:39


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	string s;
	for(int i = 0; i < n; i++){
		cin >> s;
		int l = s.length();
		cout << l;
		if(s.length() >= 10){
			cout << s[0] << s.length() - 2 << s[l- 1];
			cout << "\n";
		}
		else{
			cout << s;
			cout << "\n";
		}
	}
	return 0;

}
