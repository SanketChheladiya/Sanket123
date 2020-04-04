#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t1;
    cin >> t1;
    for(int t = 1; t <= t1; ++t)
    {
        int n;
        cin >> n;
        vector<pair<int,int>> activity;
        int arr[n][2];
        char res[n];
        for(int i = 0; i < n; ++i)
        {
            cin >> arr[i][0] >> arr[i][1];
            activity.push_back(make_pair(arr[i][0],i));
        }
        
        sort(activity.begin(), activity.end());
        
        int cami = 0, jam = 0;
        bool fg = false;
        for(int i = 0; i < n; ++i)
        {
            if(activity[i].first >= cami)
            {
                res[activity[i].second] = 'C';
                cami = arr[activity[i].second][1];
            }
            else
            {
                if(activity[i].first >= jam)
                {
                    res[activity[i].second] = 'J';
                    jam = arr[activity[i].second][1];
                }
                else
                {
                    fg = true;
                    break;
                }
            }
        }
        if(fg)
        {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #"<< t << ": ";
            for(int i = 0; i < n; ++i)
            {
                cout<<res[i];
            }
            cout << '\n';
        }
    }
}
