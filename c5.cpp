#include <bits/stdc++.h>
using namespace std;
int powerof2(int n)
{
while(n>1){
    int l=n%2;
    if(l!=0)
    return 0;
    n=n/2;
}
return 1;
}
int max1(int n){
    int max=n;
for(int i=n;i>=0;i--){
    if(powerof2(i)==1){
        max=i;break;}
}
return max;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n];int b[n];
        for(int i=0;i<n;i++)
        a[i]=i;
        int l=max1(n-1);
        int k=n-l-1;
        for(int i=0;i<l;i++)
        b[i]=l-i-1;
        for(int i=l;i<n;i++)
        b[i]=i;
        for(int i=0;i<n;i++)
        cout<<b[i]<<" ";
        cout<<endl;
    }
}