/***
/*
    description: A

    author:    lepindev
    created:   10.03.2023 23:32:52


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	int t = 0;
	if(a == b){
		cout << 1;
		return 0;
	}
	while(a <= b){
		b = b * 2;
		a = a * 3;
		t++;
	}
	cout << t;
	return 0;
}
