
#include <iostream>

using namespace std;

int main() {
  int n, secret;
  cin >> n >> secret;

  int count = 0;
  for (int i = 1; i <= n; ++i) {
    if (secret % i == 0) {
      count++;
    }
  }

  cout << count << endl;

  return 0;
}