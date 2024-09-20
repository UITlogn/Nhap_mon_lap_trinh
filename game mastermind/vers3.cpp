#include <bits/stdc++.h>                                                                                                                                                                                      //Logm
using namespace std;

const int N = 4, M = 8;

vector<int> a, ans;

vector<vector<int> > state;

int count1(vector<int> &x, vector<int> &y) {
    int cnt = 0;
    for (int i = 0; i < N; ++i)
        cnt += (x[i] == y[i]);
    return cnt;
}

int count2(vector<int> &x, vector<int> &y, int msk) {
    int cnt = 0;
    for (int i = 0; i < N; ++i)
        if (x[i] != y[i] && msk >> x[i] & 1)
            ++cnt;
    return cnt;
}

vector<int> dt;
int msk;
void backtrack(int i) {
    if (i == N) {
        state.push_back(dt);
        return;
    }
    for (int x = 0; x < M; ++x) if ((msk >> x & 1) == 0) {
        msk ^= 1 << x;
        dt.push_back(x);
        backtrack(i + 1);
        dt.pop_back();
        msk ^= 1 << x;
    }
}

struct query {
    vector<int> a;
    int cnt1, cnt2;
    int msk;
    void build() {
        msk = 0;
        for (int i = 0; i < a.size(); ++i) {
            msk |= 1 << a[i];
        }
    }
};
vector<query> h;

bool check(vector<int> &s) {
    for (query &t: h) {
        int cnt1 = count1(s, t.a);
        int cnt2 = count2(s, t.a, t.msk);
        if (cnt1 != t.cnt1 || cnt2 != t.cnt2)
            return 0;
    }
    return 1;
}
vector<int> guess() {
    for (vector<int> &s: state)
        if (check(s))
            return s;
    return vector<int>(N, 0);
}
signed main() {
    backtrack(0);

    cout << "Version 2: Play guessing online" << endl;
    cout << "You have to write down a key consisting of 4 different digits, each digit from 0 to 7." << endl;
    cout << "The computer are trying to guess your key" << endl;
    cout << "With each guess, you have to input to the computer how many positions match the key," << endl;
    cout << "and how many numbers appear in the key but not in the correct position. " << endl;
    cout << "#############################################" << endl;
    
    while (1) {
        cout << "Guess: ";
        a = guess();
        for (int i = 0; i < N; ++i) cout << a[i] << ' '; cout << endl;
        // 6 2 5 3
        int cnt1, cnt2; cin >> cnt1 >> cnt2;
        query tmp;
        tmp.a = a;
        tmp.cnt1 = cnt1;
        tmp.cnt2 = cnt2;
        tmp.build();
        h.push_back(tmp);

        if (cnt1 == N) {
            cout << "___WIN___" << endl;
            system("pause");
            return 0;
        }
    }
    return 0;
}