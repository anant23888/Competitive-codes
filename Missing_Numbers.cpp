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
    int p = -99999, p1 = -99999, p2 = -9999, p3 = -99999,p4=-99999,p5=-99999;
    int k = (arr[0] + arr[2]) / 2;
    int k1 = arr[2] - k;
    if (k1 > 0)
    {
        p = (k / k1);
    }
    int k2 = (arr[1] + arr[2]) / 2;
    int k3 = arr[2] - k2;
    if (k3 > 0)
    {
        p1 = (k2 / k3);
    }
    int k4 = (arr[0] + arr[1]) / 2;
    int k5 = arr[1] - k4;
    if (k5 > 0)
    {
        p2 = (k4 / k5);
    }
    int k7 = (arr[0] + arr[3]) / 2;
    int k6 = arr[3] - k7;
    if (k6 > 0)
    {
        p3 = (k7 / k6);
    }
    int k8=(arr[1]+arr[3])/2;
    int k9=(arr[3]-k8);
    if(k9>0){
        p4=(k8/k9);
    }
    if (k * k1 == arr[3] && arr[1] == p&&k<=10000&&k1<=10000)
        cout << k << " " << k1 << ln;
    else if (k2 * k3 == arr[3] && arr[0] == p1&&k2<=10000&&k3<=10000)
        cout << k2 << " " << k3 << ln;
    else if (k4 * k5 == arr[3] && arr[2] == p2&&k4<=10000&&k5<=10000)
        cout << k4 << " " << k5 << ln;
    else if (k7 * k6 == arr[2] && arr[1] == p3&&k7<=10000&&k6<=10000)
        cout << k7 << " " << k6 << ln;
    else if (k7 * k6 == arr[1] && arr[2] == p3&&k7<=10000&&k6<=10000)
        cout << k7 << " " << k6 << ln;
    else if(k8*k9==arr[2]&&arr[0]==p4&&k8<=10000&&k9<=10000)
        cout<<k8<<" "<<k9<<ln;
    else if(k8*k9==arr[0]&&arr[2]==p4&&k8<=10000&&k9<=10000)
        cout<<k8<<" "<<k9<<ln;   
    else
        cout << -1 << " " << -1 << ln;
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