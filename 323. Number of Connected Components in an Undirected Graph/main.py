from typing import List

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.root = [i for i in range(N)]
        self.rank = [1] * N
        self.cnt = N

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ufind = UnionFind(n)
        for e in edges:
            ufind.union(e[0], e[1])
        print(ufind.root)
        return ufind.getCnt()

if __name__ == "__main__":
    sol = Solution()
    
    # n = 5
    # edges = [[0,1],[1,2],[3,4]]
    # print(sol.countComponents(n,edges))

    # n = 5
    # edges = [[0,1],[1,2],[2,3],[3,4]]
    # print(sol.countComponents(n,edges))

    n = 5
    edges = [[0,1],[1,2],[0,2],[3,4]]
    print(sol.countComponents(n,edges))
