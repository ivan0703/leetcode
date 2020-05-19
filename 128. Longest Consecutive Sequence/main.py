from typing import List

class Solution:
    def count(self, key, uset):
        if key not in uset:
            return 0
        else:
            uset.remove(key)
            return 1 + self.count(key+1, uset) + self.count(key-1, uset)

    def longestConsecutive(self, nums: List[int]) -> int:
        uset = set(nums)
        res = 0
        while uset:
            e = list(uset)[0]
            res = max(res, self.count(e,uset))
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))