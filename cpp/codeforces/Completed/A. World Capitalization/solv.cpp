/***
/*
    description: A

    author:    lepindev
    created:   08.03.2023 20:55:25


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	string s;
	cin >> s;       
	if(s[0] >= 'a' && s[0] <= 'z'){
		s[0] = s[0] - 32;
	}
	cout << s;
	return 0;
}
