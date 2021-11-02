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

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        if len(edges) != n - 1:
            return False

        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for e in edges:
            self.union(e[0],e[1])
        
        r = self.find(0)
        for i in range(1,n):
            if r != self.find(i):
                return False

        return True

if __name__ == "__main__":
    sol = Solution()

    # n = 5
    # edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

    n = 2
    edges = []
    print(sol.validTree(n, edges))