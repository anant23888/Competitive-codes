#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
        int n;
	    cin>>n;
	    string s;
	    cin>>s;int c=0;int c1;
		for(int i=0;i<n;i++)
		{
			if(s[i]=='0')
			c++;
		}
		c1=n-c;
		if(c==c1)
		cout<<n<<endl;
		else if(c<c1)
		cout<<(c+1)<<endl;
		else if(c>c1)
		cout<<(c1+1)<<endl;

	}
	return 0;
}
