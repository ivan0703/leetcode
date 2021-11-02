from typing import List

class Solution:
    def __init__(self):
        self.root = []
        self.rank = []

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            else:
                self.root[rx] = ry
                self.rank[ry] += 1


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        self.root = [i for i in range(N)]
        self.rank = [1] * N

        for i in range(N-1):
            for j in range(i+1, N):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        
        cnt = set()
        for i in range(N):
            cnt.add(self.find(i))
        
        return len(cnt)
        
if __name__ == "__main__":
    sol = Solution()
    # isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    # isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(sol.findCircleNum(isConnected))