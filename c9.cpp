#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int powerof2(long long int n)
{
while(n>1){
    int l=n%2;
    if(l!=0)
    return 0;
    n=n/2;
}
return 1;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    long long int n;
	    cin>>n;long long int i;
	    for( i=n;i>=2;i--){
	        if(powerof2(i)==1)
	        break;
	    }
	    i=i*2;int a[3];long long int k=i-n;a[2]=n;
	    a[0]=k;a[1]=k+1;
	    for(int i=0;i<3;i++)
	    cout<<a[i]<<" ";
	    cout<<endl;
	}
	return 0;
}
