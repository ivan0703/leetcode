from typing import List
import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        w = []
        for i,v in enumerate(nums):
            if len(w) == k+1:
                w.remove(nums[i-k-1])
            
            idx = bisect.bisect_left(w,v)
            w.insert(idx,v)

            left  = bisect.bisect_left(w, v-t)
            right = bisect.bisect_right(w, v+t)
            if right-left>1:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    print(sol.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
    print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))

