#include <bits/stdc++.h>
using namespace std;
int check(string s,int n){
	int l=n/2;int c=0;
	for(int i=0;i<l;i++){
		if(s[i]!=s[n-1-i])
		c++;
	}
	return c;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,k;
	    cin>>n>>k;
	    string s;
		cin>>s;
        int l=n/2;
        int c=check(s,n);
			if(k==c)
            cout<<"YES"<<endl;
            else
            cout<<"NO"<<endl;
	}
	return 0;
}
