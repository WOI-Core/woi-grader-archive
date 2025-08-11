
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> scrolls(n);
    for (int i = 0; i < n; ++i) {
        cin >> scrolls[i];
    }

    sort(scrolls.begin(), scrolls.end());

    int sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += scrolls[i];
    }

    cout << sum << endl;

    return 0;
}