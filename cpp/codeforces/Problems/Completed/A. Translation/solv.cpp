/***
/*
    description: A

    author:    lepindev
    created:   11.03.2023 22:30:08


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	string s, t;
	cin >> s >> t;
	string a;
	for(int i = s.length() - 1; i >= 0; i--){
		a += s[i];
	}
	if(a == t){
		cout << "YES";
	}
	else{
		cout << "NO";
	}

	return 0;
}
