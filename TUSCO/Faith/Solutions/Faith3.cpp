#include <bits/stdc++.h>
#define coutf(n, m) cout << fixed << setprecision(n) << m
#define forr(i, a, n) for (int i = a; i < n; i++)
#define forl(i, a, n) for (int i = a; i > n; i--)
#define macos ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define endll "\n"
#define sp " "
typedef long long ll;
using namespace std;

ll solve(ll i, ll cnt, ll d){
    if(abs(i)>d)return LLONG_MAX;
    if(i == d)return cnt;
    return min(solve(i-cnt-1,cnt+1,d),solve(i+cnt+1,cnt+1,d));
}

int main(){macos;

    int t;
    cin >> t;
    while(t--){
        ll d;
        cin >> d;
        d = abs(d);
        cout << solve(0,0,d) << endll;
    }

    return 0;
}