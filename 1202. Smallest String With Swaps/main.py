from typing import List

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ufind = UnionFind(len(s))
        for p in pairs:
            ufind.union(p[0], p[1])
        m = {}
        for i in range(len(s)):
            r = ufind.find(i)
            if r not in m:
                m[r] = [[i],[s[i]]]
            else:
                m[r][0].append(i)
                m[r][1].append(s[i])

        ret = [c for c in s]
        for k, v in m.items():
            v[0].sort()
            v[1].sort()
            for i in range(len(v[0])):
                ret[v[0][i]] = v[1][i]
        str =  ''.join(ret)
        return str

if __name__ == "__main__":
    sol = Solution()

    s = "dcab"
    pairs = [[0,3],[1,2]]
    print(sol.smallestStringWithSwaps(s, pairs))

    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    print(sol.smallestStringWithSwaps(s, pairs))

    s = "cba"
    pairs = [[0,1],[1,2]]
    print(sol.smallestStringWithSwaps(s, pairs))
