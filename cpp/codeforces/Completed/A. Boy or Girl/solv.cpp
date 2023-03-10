/***
/*
    description: A

    author:    lepindev
    created:   08.03.2023 21:26:15


***/
// sevenkplus
// s e v n k p l u 

#include <bits/stdc++.h>

using namespace std;

int main() {
	string s;
	cin >> s;
	int n = s.length();
	int count = 0;
	sort(s.begin(), s.end());
	for(int i = 0; i < n; i++){
		if(s[i] != s[i+1]){
			count++;
		}
	}
	if(count % 2 == 0){
		cout << "CHAT WITH HER!";
	}
	else{
		cout << "IGNORE HIM!";
	}
	return 0;
}
