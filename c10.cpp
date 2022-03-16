#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int check(string s,int n){
	int l=n/2;
	for(int i=0;i<l;i++){
		if(s[i]!=s[n-1-i])
		return 0;
	}
	return 1;
}
int convert(string s,int n,int k){
	int l=n/2;int i=0;
	for(int j=0;i<k&&j<l;j++){
		if(s[i]!=s[n-1-i]){
		s[i]=s[n-1-i];i++;}
	}
	if(i==k&&check(s,n)==1)
	return 1;
	else
	return 0;
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
			if(convert(s,n,k)==1)
			cout<<"YES"<<endl;
			else
			cout<<"NO"<<endl;
	}
	return 0;
}
