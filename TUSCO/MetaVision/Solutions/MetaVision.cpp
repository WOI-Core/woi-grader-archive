#include<iostream>

long long fibo[1000001];

int main(){
    int N;
    std::cin >> N;

    const int MOD = 1e9+7;

    fibo[0] = fibo[1] = 1;
    for(int i = 2; i <= N; i++){
        fibo[i] = (fibo[i-1] + fibo[i-2]) % MOD;
    }

    std::cout << fibo[N];

    return 0;
}