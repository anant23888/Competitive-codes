#include<bits/stdc++.h>
using namespace std;
#define lint long long int
int main(){
    int T;
    cin>>T;
    while(T--){
        lint n;
        cin>>n;
        string s;
        
        for(lint i=0;i<n;i++){
            cin>>s[i];
        }
        lint count=0;
        for(lint i=0;i<n/2;i++){
            if(s[i]!=s[n-1-i]){
                count++;
            }
        }
        cout<<count<<endl;
    }
}