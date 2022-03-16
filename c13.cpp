#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,a,b,c;
	    cin>>x>>a>>b>>c;
	    int temp=a;int max=a;
	    if(b<=temp&&c>=b)
	    temp=b;
	    else if(c<=temp&&c<=b)
	    temp=c;
	    if(b>max&&b>c)
	    max=b;
	    else if(c>max&&c>b)
	    max=c;
	    long long int price=(x)*temp;max-=temp;
	    a-=temp;b-=temp;c-=temp;int d=0;
	        if(a<max&&a>0)
	        price+=a;
	        else if(b<max&&b>0)
	        price+=b;
	        else if(c<max&&c>0)
	        price+=c;
	    cout<<price<<endl;
	}
	return 0;
}
