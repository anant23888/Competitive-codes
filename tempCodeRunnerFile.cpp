#include<bits/stdc++.h>
using namespace std;

#define nl "\n"

int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int x;
        cin>>x;
        int a[3];
        for(int i=0;i<3;i++){
            cin>>a[i];
        }
        int j;
        int min1 =a[0];
        for(int i=1;i<3;i++){
            if(a[i]<min1){
                j=i;
                min1=a[i];
            }
        }
        a[j]=9999;
        int min2=a[0];
        for(int i=0;i<3;i++){
            if(a[i]<min2){
                min2 = a[i];
            }
        }
        int res = min1*(x-1)+min2;
        cout<<res<<nl;
    }
}