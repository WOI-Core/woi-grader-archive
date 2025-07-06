
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> crystals(n);
    for (int i = 0; i < n; ++i) {
        cin >> crystals[i];
    }

    int total_power = 0;
    for (int energy : crystals) {
        total_power += energy;
    }

    cout << total_power << endl;

    return 0;
}