from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sum = 0
        max_sum = 0
        win_start, win_end = 0, 0 + X -1
        for i,c in enumerate(customers):
            if i>=win_start and i<=win_end:
                sum += c
            elif grumpy[i] == 0:
                sum += customers[i]
        max_sum = sum

        if win_start > win_end:
            return max_sum

        # slide the window
        next_win_start = win_start + 1
        next_win_end = win_end + 1
        while next_win_end < len(customers):
            if grumpy[win_start] == 1:
                sum -= customers[win_start]
            if grumpy[next_win_end] == 1:
                sum += customers[next_win_end]
            max_sum = max(max_sum, sum)

            win_start = next_win_start
            win_end = next_win_end
            next_win_start += 1
            next_win_end += 1

        return max_sum
    
if __name__ == "__main__":
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    X = 3
    
    sol = Solution()
    print(sol.maxSatisfied(customers, grumpy, X))