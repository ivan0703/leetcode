#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        int idx = nums.size();
        while(left <= right) {
            int mid = (right + left) / 2;
            if(nums[mid] == target) {
                idx = mid;
                break;
            } else if(nums[mid] > target) {
                idx = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return idx;
    }
};

int main()
{
    Solution sol;
    vector<int> nums;
    int target;

    nums = {1,3,5,6};
    target = 5;
    cout<<sol.searchInsert(nums, target)<<endl;

    nums = {1,3,5,6};
    target = 2;
    cout<<sol.searchInsert(nums, target)<<endl;

    nums = {1,3,5,6};
    target = 7;
    cout<<sol.searchInsert(nums, target)<<endl;

    nums = {1,3,5,6};
    target = 0;
    cout<<sol.searchInsert(nums, target)<<endl;

    return 0;
}