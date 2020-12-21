#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        vector<int> ret;
        map<int,int> htmap = {{0,0}};

        int max_height = 0;
        for(auto &pos : positions) {
            auto left  = htmap.lower_bound(pos[0]);
            auto right = htmap.lower_bound(pos[0]+pos[1]);
            int h = 0;

            auto it = left;
            if(left->first!=pos[0]) {
                it--;
            }
            for(; it != right; it++) {
                h = max(h, it->second);
            }

            map<int,int> intl;
            intl.insert({pos[0], h + pos[1]});
            intl.insert({pos[0]+pos[1], prev(right,1)->second});
            htmap.erase(left,right);
            htmap.insert(intl.begin(), intl.end());

            max_height = max(max_height, h + pos[1]);
            ret.push_back(max_height);
        }
        
        return ret;
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> positions;
    vector<int> ret;

    positions = { {1, 2}, {2, 3}, {6, 1} };
    ret = sol.fallingSquares(positions);
    for(auto i : ret) {
        cout<<i<<" ";
    }
    cout<<endl;


    positions = { {100, 100}, {200, 100} };
    ret = sol.fallingSquares(positions);
    for(auto i : ret) {
        cout<<i<<" ";
    }
    cout<<endl;

    positions = { {6,1},{9,2},{2,4} };
    ret = sol.fallingSquares(positions);
    for(auto i : ret) {
        cout<<i<<" ";
    }
    cout<<endl;

    positions = { {1,5},{2,2},{7,5} };
    ret = sol.fallingSquares(positions);
    for(auto i : ret) {
        cout<<i<<" ";
    }
    cout<<endl;

    return 0;
}