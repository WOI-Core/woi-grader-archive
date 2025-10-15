#include <bits/stdc++.h>
#define coutf(n, m) cout << fixed << setprecision(n) << m
#define forr(i, a, n) for (int i = a; i < n; i++)
#define forl(i, a, n) for (int i = a; i > n; i--)
#define macos ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define endll "\n"
#define sp " "
typedef long long ll;
using namespace std;

int main(){macos;

    int t;
    cin >> t;

    while(t--){
        ll d, l = 0, r = 2e10;
        cin >> d;
        d = abs(d);
        
        while(l<r){
            ll m = (l + r) / 2;
            if(m*(m+1)/2<d)l = m + 1;
            else r = m;
        }
        
        if(d%2==ll(ceil(l/2.0))%2)cout << l;
        else if(l&1)cout << l+2;
        else cout << l+1;
        cout << endll;
    }

    return 0;
}