/***
/*
    description: A

    author:    lepindev
    created:   11.03.2023 21:07:36


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	string s;
	cin >> n >> s;
	int a = 0;
	int d = 0;
	for(int i = 0; i < s.length(); i++){
		if(s[i] == 'D'){
			d++;
		}
		if(s[i] == 'A'){
			a++;
		}
	}
	if(d > a){
		cout << "Danik";
	}
	else if(a > d){
		cout << "Anton";
	}
	else{
		cout << "Friendship";
	}
	return 0;
}
