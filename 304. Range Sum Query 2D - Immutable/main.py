from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [x[:] for x in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    self.dp[i][j] += self.dp[i-1][j]
                if j > 0:
                    self.dp[i][j] += self.dp[i][j-1]
                if i > 0 and j > 0:
                    self.dp[i][j] -= self.dp[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.dp[row2][col2]
        if row1 > 0:
            ans -= self.dp[row1-1][col2]
        if col1 > 0:
            ans -= self.dp[row2][col1-1]
        if row1 > 0 and col1 > 0:
            ans += self.dp[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    numMat = NumMatrix(matrix)
    print(numMat.sumRegion(2, 1, 4, 3))
    print(numMat.sumRegion(1, 1, 2, 2))
    print(numMat.sumRegion(1, 2, 2, 4))
