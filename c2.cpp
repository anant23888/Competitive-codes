#include <bits/stdc++.h>
using namespace std;
int check(int a[],int n){
    for(int i=0;i<n-1;i++){
        if(a[i]!=a[i+1])
        return 0;
    }
    return 1;
}
int main(){
    int t;
    cin>>t;
    while(t-->0){
        int n;
        cin>>n;int k=1;int l=1;int a[n];int d=0;
        for(int i=0;i<n;i++)
        cin>>a[i];
       for(int i=0;i<n&&k<n&&l<n;i++){
           int p=2*k;
           for(int j=0;j<p;j++){
               if(check(a,n)==0){
              for(int z=0;z<k;z++)
                  a[l+k+i]=a[l+i];
               d++; }k+=1;
       }
       l+=1;
        }
        cout<<d<<endl;
    }
}