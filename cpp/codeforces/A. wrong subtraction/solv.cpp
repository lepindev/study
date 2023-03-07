/***
/*
    description: True Template

    author:    lepindev
    created:   07.03.2023 18:20:43


***/
#include <iostream>
using namespace std;
int main() {
	int n, k;
	cin >> n >> k;
	for(int i = 0; i < k; i++) {
		if(n % 10 != 0) {
			n--;
		}
		else {
			n = n / 10;
		}
	}
	cout << n;
}