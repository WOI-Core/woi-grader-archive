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
        ll d, cnt = 0, sum = 0;
        cin >> d;
        d = abs(d);
        while(sum<d || (sum-d)&1){
            cnt++;
            sum += cnt;
        }
        cout << cnt << endll;
    }

    return 0;
}