#include<bits/stdc++.h>

using namespace std;

int main(){
    
    double n ; cin >> n ;
    double res = 1 ;

    for(int i = 1 ; i <= 365 ; i++){

        res *= double (365 - i + 1) / double (365) ;

        if(1 - res >= n){
            cout << i << "\n";
            break;
        }
    }

    return 0;
}