
#include <iostream>
#include <string>

using namespace std;

int main() {
  string s, t;
  cin >> s >> t;

  int hamming_distance = 0;
  for (size_t i = 0; i < s.length(); ++i) {
    if (s[i] != t[i]) {
      hamming_distance++;
    }
  }

  cout << hamming_distance << endl;

  return 0;
}