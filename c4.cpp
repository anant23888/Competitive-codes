#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        int l=s.length();
        if(l==1)
        cout<<"YES"<<endl;
        else if(l==2&&s!="00"&&s!="11")
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
    }
}