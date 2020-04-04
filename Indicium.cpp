#include <bits/stdc++.h>

using namespace std;

int sqr[60][60], n, k, t;
bool row_safe[60][60], col_safe[60][60], sol;

void solver(int r, int c, int m) {
    if (r == n && c == n + 1 && m == k && !sol) {
        sol = true;
        cout << "Case #" << t << ": " << "POSSIBLE\n";
        for (int i = 1; i <= n; ++i) 
	{
            for (int j = 1; j <= n; ++j) 
		{
                cout << sqr[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    } else if (r > n) {
        return;
    } else if (c > n) {
        solver(r + 1, 1, m);
    }
    for (int i = 1; i <= n && !sol; ++i) {
        if (!row_safe[r][i] && !col_safe[c][i]) {
            row_safe[r][i] = col_safe[c][i] = true;
            if (r == c) {
                m += i;
            }
            sqr[r][c] = i;

            solver(r, c + 1, m);

            row_safe[r][i] = col_safe[c][i] = false;
            if (r == c) {
                m -= i;
            }
            sqr[r][c] = 0;
        }
    }
}

int main() {
    int T;
    scanf(" %d", &T);
    for (t = 1; t <= T; ++t) {
        scanf(" %d %d", &n, &k);
        solver(1, 1, 0);
        if (!sol) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }
        sol = false;
    }
    return 0;
}
