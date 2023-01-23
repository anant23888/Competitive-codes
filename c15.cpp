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
typedef pair<int, int> p32;
typedef pair<ll, ll> p64;
typedef pair<double, double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int>> vv32;
typedef vector<vector<ll>> vv64;
typedef vector<vector<p64>> vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i, e) for (ll i = 0; i < e; i++)
#define forsn(i, s, e) for (ll i = s; i < e; i++)
#define rforn(i, s) for (ll i = s; i >= 0; i--)
#define rforsn(i, s, e) for (ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout << #x << " = " << x << ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin()                    \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())

void solve()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int arr[4];
    arr[0] = a;
    arr[1] = b;
    arr[2] = c;
    arr[3] = d;
    sort(arr, arr + 4);
    if (a < 0 || b < 0 || c < 0 || d < 0)
    {
        int p=-2,p1=-2,p2=-2;
        int k = (arr[0] + arr[2]) / 2;
        int k1 = arr[0] - k;
        int k4=arr[2]-k;
        int k2 = (arr[0] + arr[1]) / 2;
        int k3 = arr[0] - k2;
        if(k1>0){
         p = floor(k / k1);}
         if(k3>0){
         p1 = floor(k2 / k3);}
         if(k4>0){
         p2=floor(k/k4);}
        if (k * k1 == arr[3] && arr[1] == p)
            cout << k << " " << k1 << ln;
        else if (k2 * k3 == arr[3] && arr[2] == p1)
            cout << k2 << " " << k3 << ln;
        else if(k*k4==arr[3]&&arr[1]==p2)
            cout<<k<<" "<<k4<<ln;    
        else
            cout << -1 << " " << -1 << ln;
    }
    else
    {
        int p=-2,p1=-2;
        int k = (arr[0] + arr[2]) / 2;
        int k1 = arr[0] - k;
        if(k1>0){
         p = floor(k / k1);}
        int k2 = (arr[1] + arr[2]) / 2;
        int k3 = arr[2] - k2;
        if(k3>0){
         p1 = floor(k2 / k3);}
        if (k * k1 == arr[3] && arr[1] == p)
            cout << k << " " << k1 << ln;
        else if (k2 * k3 == arr[3] && arr[0] == p1)
            cout << k2 << " " << k3 << ln;
        else
            cout << -1 << " " << -1 << ln;
    }
}
int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        //  cout << "Case #" << it+1 << ": ";
        solve();
    }
    return 0;
}