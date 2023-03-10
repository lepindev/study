/***
/*
    description: A

    author:    lepindev
    created:   10.03.2023 23:14:25


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	string s;
	cin >> n >> s;
	int t = 0;
	for(int i = 0; i < n - 1;i++){
		if(s[i] == s[i + 1]){
			t++;
		}
	}
	cout << t;
	return 0;
}
