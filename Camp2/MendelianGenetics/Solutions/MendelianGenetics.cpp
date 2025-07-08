
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int k, m, n;
  cin >> k >> m >> n;

  double total = k + m + n;
  double prob = 1.0;

  // Case 1: Two homozygous recessive (nn)
  prob -= (n / total) * ((n - 1) / (total - 1));

  // Case 2: Two heterozygous (Mm)
  prob -= (m / total) * ((m - 1) / (total - 1)) * 0.25;

  // Case 3: One heterozygous and one homozygous recessive
  prob -= (m / total) * (n / (total - 1)) * 0.5;
  prob -= (n / total) * (m / (total - 1)) * 0.5;

  cout << fixed << setprecision(5) << prob << endl;

  return 0;
}