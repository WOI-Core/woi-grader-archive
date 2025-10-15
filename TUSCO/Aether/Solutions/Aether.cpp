#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1e6;
ll pre[N + 1];

int main() {ios::sync_with_stdio(0); cin.tie(0);
    for (ll i = 1; i <= N; i++) pre[i] = (2 * i - 1) * (2 * i - 1) + pre[i - 1];
    int t;
    cin >> t;
    while (t--) {
        ll cp, ir, gd, dm;
        cin >> cp >> ir >> gd >> dm;
        ll n = cp + ir + gd + dm;
        int h = upper_bound(pre + 1, pre + N + 1, n) - pre - 1;
        ll blocks = pre[h];
        ll used_cp = 0, used_ir = 0, used_gd = 0, used_dm = 0;
        used_cp = min(cp, blocks);
        blocks -= used_cp;
        if(blocks){
            used_ir = min(ir, blocks);
            blocks -= used_ir;
        }
        if(blocks){
            used_gd = min(gd, blocks);
            blocks -= used_gd;
        }
        if(blocks) used_dm = min(dm, blocks); 
        ll left_cp = cp - used_cp, left_ir = ir - used_ir, left_gd = gd - used_gd, left_dm = dm - used_dm;
        ll rest = left_cp + left_ir*5 + left_gd*20 + left_dm*100;
        cout << h << " " << rest << "\n";
    }
    return 0;
}