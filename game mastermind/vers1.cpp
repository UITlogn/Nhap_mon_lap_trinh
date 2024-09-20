#include <bits/stdc++.h>                                                                                                                                                                                      //Logm
using namespace std;

mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());
int Rand(int l, int r) {
    return l + rd() % (r - l + 1);
}

const int N = 4, M = 8;

int a[N], ans[N];
int mskans;

int count1() {
    int cnt = 0;
    for (int i = 0; i < N; ++i)
        cnt += (a[i] == ans[i]);
    return cnt;
}

int count2() {
    int cnt = 0;
    for (int i = 0; i < N; ++i)
        if (a[i] != ans[i] && (mskans >> a[i] & 1))
            ++cnt;
    return cnt;
}

signed main() {
    cout << "Version 1: People guessing" << endl;
    cout << "The computer is storing a key consisting of 4 different digits, each digit from 0 to 7." << endl;
    cout << "You do not know the key and have to make a guess." << endl;
    cout << "With each guess, the computer will tell you how many positions match the key," << endl;
    cout << "and how many numbers appear in the key but not in the correct position. " << endl;
    cout << "#############################################" << endl;

    for (int i = 0; i < N; ++i) {
        ans[i] = Rand(0, M - 1);
        while (mskans >> ans[i] & 1) {
            ans[i] = Rand(0, M - 1);
        }
        mskans |= 1 << ans[i];
    }

    cout << "KEY: ";
    for (int i = 0; i < N; ++i) cout << "? "; cout << endl;

    while (1) {
        cout << "Guess: ";
        for (int i = 0; i < N; ++i) cin >> a[i];

        int cnt1 = count1(), cnt2 = count2();
        cout << cnt1 << ' ' << cnt2 << '\n';
        if (cnt1 == N) {
            cout << "___WIN___";
            break;
        }
    }
    
    system("pause");
    system("pause");
    system("pause");
    system("pause");
    return 0;
}