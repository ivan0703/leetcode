#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<long long> st;
        for(int i=0,j=0; i<nums.size(); i++) {
            if(st.size()==k+1) {
                st.erase(nums[j]);
                j++;
            }
            auto it_h = st.upper_bound(nums[i]+(long long)t);
            auto it_l = st.lower_bound(nums[i]-(long long)t);
            if(it_h!=it_l)
                return true;
            st.insert(nums[i]);
        }
        return false;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1,2,3,1};
    cout<<sol.containsNearbyAlmostDuplicate(nums, 3, 0)<<endl;

    nums = {1,0,1,1};
    cout<<sol.containsNearbyAlmostDuplicate(nums, 1, 2)<<endl;

    nums = {1,5,9,1,5,9};
    cout<<sol.containsNearbyAlmostDuplicate(nums, 2, 3)<<endl;

    nums = {2147483640,2147483641};
    cout<<sol.containsNearbyAlmostDuplicate(nums, 1, 100)<<endl;

    return 0;
}