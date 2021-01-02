#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        int ret = 0;
        vector<int> nums;
        for(int i : instructions) {
            auto lower = lower_bound(nums.begin(), nums.end(), i);
            auto upper = upper_bound(nums.begin(), nums.end(), i);
            int left = distance(nums.begin(), lower);
            int right = distance(upper, nums.end());
            ret += min(left,right);
            nums.insert(lower,i);
        }
        return ret;
    }
};


int main()
{
    Solution sol;
    vector<int> instructions = {1,5,6,2};
    cout<<sol.createSortedArray(instructions)<<endl;

    instructions = {1,3,3,3,2,4,2,1,2};
    cout<<sol.createSortedArray(instructions)<<endl;

    return 0;
}