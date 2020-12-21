from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -float('Inf')

        ans = nums[0]
        dp = nums[0] # max sub-array sum ended at i
        for i in range(1,len(nums)):
            dp = max(nums[i], dp+nums[i])
            ans = max(ans, dp)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([]))
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))