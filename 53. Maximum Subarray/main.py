from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -float('Inf')

        ans = nums[0]
        dp = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1,len(dp)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            ans = max(ans, dp[i])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([]))
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))