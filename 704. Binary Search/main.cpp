#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int helper(vector<int>& nums, int target, int start, int end) {
        if (start > end) {
            return -1;
        }
        
        int mid = start + (end-start) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            return helper(nums, target, mid+1, end);
        } else {
            return helper(nums, target, start, mid-1);
        }        
    }

    int search(vector<int>& nums, int target) {
        return helper(nums, target, 0, nums.size() - 1);
    }
};

int main()
{
    Solution sol;
    
    int target;
    vector<int> nums;
        
    target = 9;
    nums = {-1,0,3,5,9,12};
    cout<<sol.search(nums, target)<<endl;

    target = 2;
    nums = {-1,0,3,5,9,12};
    cout<<sol.search(nums, target)<<endl;

    target = 13;
    nums = {-1,0,3,5,9,12};
    cout<<sol.search(nums, target)<<endl;

    target = -1;
    nums = {-1,0,3,5,9,12};
    cout<<sol.search(nums, target)<<endl;

    target = 12;
    nums = {-1,0,3,5,9,12};
    cout<<sol.search(nums, target)<<endl;
}