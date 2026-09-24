#include <bits/stdc++.h>
using namespace std;

int main() {
    int i, j, n;

    cout << "Enter the number: ";
    cin >> n;

    for (i=0; i<n; i++) {
        // Print spaces
        for (j=0; j <(n-i-1); j++) {
            cout << " ";
        }
        // Print stars
        for (j=0; j<(2*i+1); j++) {
            cout <<"*";
        }
        for (j=0; j <(n-i-1); j++) {
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}
