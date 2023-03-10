/***
/*
    description: A

    author:    lepindev
    created:   10.03.2023 22:49:51


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n,k;
	cin >> n >> k;
	int a[n];
	for(int i = 0; i < n; i++){
		cin >> a[i];
	}
	int t = 0;
	for(int j = 0; j < n; j++){     
		if(a[j] > 0 && a[j] >= a[k - 1]){
			t++;
		}
	}
	cout << t;
	return 0;
}
