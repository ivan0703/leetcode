from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        uset = set()
        for n in nums:
            if n in uset:
                ans.append(n)
            else:
                uset.add(n)
        return ans

if __name__ == "__main__":
    sol = Solution()
    ans = sol.findDuplicates([4,3,2,7,8,2,3,1])
    for n in ans:
        print(n)