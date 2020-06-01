#include <iostream>
#include <vector>
#include <map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {

        vector<int> res(positions.size(), 0);
        vector<int> height(positions.size(),0);
        map<int,int> headmap, tailmap;
        for(int i=0; i<positions.size(); i++) {
            int h = positions[i][1];
            unordered_set<int> uset;
            auto it = tailmap.upper_bound(positions[i][0]);
            for(;it!=tailmap.end();it++) {
                uset.insert(it->second);
            }
            auto it_end = headmap.upper_bound(positions[i][0]+positions[i][1]);
            if(it_end!=headmap.begin() && 
               prev(it_end)->first==positions[i][0]+positions[i][1]) {
                it_end = prev(it_end);
            }
            for(auto p = headmap.begin(); p!=it_end; p++) {
                if(uset.count(p->second)) {
                    h = max(h, height[p->second]+positions[i][1]);
                }
            }

            headmap[positions[i][0]] = i;
            tailmap[positions[i][0]+positions[i][1]] = i;
            height[i] = h;
            res[i] = h;
            if(i>0) {
                res[i] = max(res[i-1], res[i]);
            }
        }

        return res;
    }
};

int main()
{
    vector<vector<int>> positions = {
        {1,2}, {2,3}, {6,1}
    };
    Solution sol;
    vector<int> res = sol.fallingSquares(positions);
    for(auto &n : res) {
        cout<<n<<endl;
    }
    return 0;
}