from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.psum = nums.copy()
        for i in range(1,len(nums)):
            self.psum[i] += self.psum[i-1]

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        for j in range(i,len(self.psum)):
            self.psum[j] += delta

    def sumRange(self, i: int, j: int) -> int:
        return self.psum[j] - (self.psum[i-1] if i>0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == "__main__":
    numAry = NumArray([1,3,5])
    print(numAry.sumRange(0,2))
    numAry.update(1,2)
    print(numAry.sumRange(0,2))
    