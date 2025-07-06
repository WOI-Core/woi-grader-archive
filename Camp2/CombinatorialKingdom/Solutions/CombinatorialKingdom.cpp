
#include <iostream>

using namespace std;

long long combinations(int n, int k) {
  if (k < 0 || k > n) {
    return 0;
  }
  if (k == 0 || k == n) {
    return 1;
  }
  if (k > n / 2) {
    k = n - k;
  }
  long long res = 1;
  for (int i = 0; i < k; ++i) {
    res = res * (n - i) / (i + 1);
  }
  return res;
}

int main() {
  int n, k;
  cin >> n >> k;
  cout << combinations(n, k) << endl;
  return 0;
}