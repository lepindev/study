/***
/*
    description: A

    author:    lepindev
    created:   08.03.2023 20:43:05


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
	double n, m, a;
	cin >> n >> m >> a;
	long long r = ceil(m / a) * ceil(n / a);
	cout << r;
	return 0;
}
