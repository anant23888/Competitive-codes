#include <bits/stdc++.h>
using namespace std;
int count(string s){
   long long int l1=0,l2=0;
    long long int l=s.length();
    for(int i=0;i<l;i++){
        if(s[i]=='0')
        l1++;
        else if(s[i]=='1')
        l2++;
    }
    if(l1==l2)
    return 0;
    else if(l1>l2)
    return l2;
    else
    return l1;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        long long int k=count(s);
        cout<<k<<endl;
    }
}