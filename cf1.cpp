#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
 int l,r,a;
    cin>>l>>r>>a;int k=l;int h=r;
    int p=a-1;
    int p1=l%a;int p2=r%a;
    int d=r-l+1;int max1=0;
    if(d<a){
        if(p2>p1)
        {
            max1=r;
        }
        else{
            while(l!=p){
            l++;}
            max1=l;
        }
        }
    else{
    while(((r%a)!=p)){
        r--;
    }
    max1=r;
    }
    int max=max1/a+max1%a;
    cout<<max<<endl;
    }
}