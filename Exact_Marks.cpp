#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>  
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int> > vv32;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define forsn(i,s,e) for(ll i = s; i < e; i++)
#define rforn(i,s) for(ll i = s; i >= 0; i--)
#define rforsn(i,s,e) for(ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout<<#x<<" = "<<x<<ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
 

void solve(){
    int n,x;
    cin>>n>>x;
    int c1=n*3;
    if(x==c1){
        cout<<"YES"<<ln;
        cout<<n<<" "<<0<<" "<<0<<ln;
    }
    else if(x==0){
        cout<<"YES"<<ln;
        cout<<0<<" "<<0<<" "<<n<<ln;
    }
    else{
        int k=x/3;
        int k1=x%3;
        int n1=k*3;int k2=k+3;int k3=k+2;
        if((x-n1==0)&&(n>=k)){
            cout<<"YES"<<ln;
            cout<<k<<" "<<0<<" "<<(n-k)<<ln;
        }
        else if(x-n1==1&&(n>=k2)){
            cout<<"YES"<<ln;
            cout<<k+1<<" "<<2<<" "<<(n-k2)<<ln;
        }
         else if(x-n1==2&&(n>=k3)){
            cout<<"YES"<<ln;
            cout<<k+1<<" "<<1<<" "<<(n-k3)<<ln;
        }
        else{
            cout<<"NO"<<ln;
        }
    }
}
int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        solve();
    }
    return 0;
}