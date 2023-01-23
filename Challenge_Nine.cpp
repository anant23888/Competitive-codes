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
typedef pair<ll,ll> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<ll> v32;
typedef vector<vector<ll> > vv32;
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
 
ll count(ll n){
    ll c=0;
    while(n>0){
        c++;
        n=n/10;
    }
    return c;
}
int * inttoarr(int n,int arr[]){
    int i=0;
while(n>0){
    arr[i]=n%10;
    i++;
    n=n/10;
}
return arr;
}
int arrtoint(int arr[],int p){
    int sum=0;int p=1;
    for(int i=0;i<p;i++){
        int l=arr[i]*p;
        sum+=arr[i];
        p=p*10;
    }
    return sum;
}
void solve(){
    ll n;
    cin>>n;
    int p=count(n);
    ll rem=n%9;
    ll n1=9-rem;
    ll k=n*10+n1;
    int arr[p+1];
    for()
    // ll rem=n%9;
    // ll n1=9-rem;
    // ll k=n*10+n1;
    // ll k1=count(n);
    // ll p=1;
    // for(ll i=1;i<=k1;i++){
    //     p*=10;
    // }
    // for(ll i=1;i<=9;i++){
    //     ll k2=p*i+n;
    //     if(k2<k&&(k2%9==0))
    //     k=k2;
    // }
    //  k=k%MOD;
    // cout<<k<<ln;
}
 main()
{
    fast_cin();
    ll t;
    cin >> t;
    for(ll it=1;it<=t;it++) {
     cout << "Case #" << it << ": ";
        solve();
    }
    return 0;
}