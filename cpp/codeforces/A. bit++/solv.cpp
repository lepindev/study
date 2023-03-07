/***
/*
    description: A

    author:    lepindev
    created:   07.03.2023 20:04:14


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	string s;
	int number = 0;
	for(int i = 0; i < n; i++){
		cin >> s;
		if(s[1] == '+'){
			number++;
		}
		else{
			number--;
		}
	}



	cout << number;
	return 0;
}
