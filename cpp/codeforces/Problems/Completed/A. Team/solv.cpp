/***
/*
    description: A

    author:    lepindev
    created:   10.03.2023 22:28:50


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int t = 0;
	for(int i = 0; i < n; i++){
		int a, b, c;
		cin >> a >> b >> c;
		int sum = a + b +c;
		if(sum >=2){
			t++;
		}
	}
	cout << t;
	return 0;
}
