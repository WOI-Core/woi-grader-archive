
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n, amount;
  cin >> n >> amount;

  vector<int> coins(n);
  for (int i = 0; i < n; ++i) {
    cin >> coins[i];
  }

  vector<int> dp(amount + 1, amount + 1);
  dp[0] = 0;

  for (int coin : coins) {
    for (int i = coin; i <= amount; ++i) {
      dp[i] = min(dp[i], dp[i - coin] + 1);
    }
  }

  if (dp[amount] > amount) {
    cout << -1 << endl;
  } else {
    cout << dp[amount] << endl;
  }

  return 0;
}