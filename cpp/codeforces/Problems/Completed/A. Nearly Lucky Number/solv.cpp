/***
/*
    description: A

    author:    lepindev
    created:   08.03.2023 22:31:21


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	string s;
	cin >> s;
	int count = 0;
	for(int i = 0; i < s.length(); i++){
		if(s[i] == '4' || s[i] == '7'){
			count++;
		}
	}
	if(count == 4 || count == 7){
		cout << "YES";
	}
	else{
		cout << "NO";
	}
	return 0;
}
