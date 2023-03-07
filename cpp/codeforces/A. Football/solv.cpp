/***
/*
    description: A

    author:    lepindev
    created:   07.03.2023 19:30:07


***/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.length();
    int k = 7;
    
    for(int i = 0; i <= n-k; i++){
    	for(int j = i; j < n - k - i; j++){
    		if(s[i] == s[j])
    		{
    			cout << "YES";
    			return 0;
    		}
    	}
    }




    cout << "NO";
	return 0;
	
}
