/***
/*
    description: A

    author:    lepindev
    created:   07.03.2023 20:25:26


***/

#include <bits/stdc++.h>
//32
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.length();
    for(int i = 0; i < n; i++){
    	s[i] = s[i] - 32;
    }
    cout << s;
	return 0;
}
