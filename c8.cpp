#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
       long long int hc,dc,hm,dm,k,w,a;
       cin>>hc>>dc;
       cin>>hm>>dm;
       cin>>k>>w>>a;
       if(k>0){
           if(w>=a)
           dc+=k*w;
           else
           hc+=k*a;
       }
       int k1=hc/dm;
       int k2=hm/dc;
       if(k1>=k2)
       cout<<"YES"<<endl;
       else
        cout<<"NO"<<endl;
    }
}