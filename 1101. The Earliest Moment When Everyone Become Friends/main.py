from typing import List

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.cnt = n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            self.cnt -= 1
    
    def getCnt(self):
        return self.cnt

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        ufind = UnionFind(n)
        logs.sort()
        for conn in logs:
            ufind.union(conn[1], conn[2])
            if ufind.getCnt() == 1:
                return conn[0]
        return -1

if __name__ == "__main__":
    sol = Solution()

    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
    n = 6
    print(sol.earliestAcq(logs, n))

    logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
    n = 4
    print(sol.earliestAcq(logs, n))

    logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
    n = 4
    print(sol.earliestAcq(logs, n))
