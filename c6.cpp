#include <bits/stdc++.h>
using namespace std;
int check(int l,int n,int c){
    int p=0;
while(n>0){
    int k1=l%10;
    int k2=n%10;
    if(k1==k2)
    p++;
    l=l/10;n=n/10;
}
if(p==c-1||p==c)
return 1;
else
return 0;
}
int count(int n){
    int c=0;
    while(n>0){
        c++;
        n=n/10;
    }
    return c;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;int c=count(n);
        if(n%7==0)
        cout<<n<<endl;
        else if(n==0)
        cout<<7<<endl;
        else{
            int k=n/7;
            int l=k*7;
             if(check(l,n,c)==0)
                 l=l+7;
            cout<<l<<endl;
        }
    }
}