from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, start, end, g, visited):
        if start == end:
            return True

        visited[start] = True
        for node in g[start]:
            if node == end:
                return True
            if not visited[node] and self.dfs(node, end, g, visited):
                return True
        return False

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end or [start,end] in edges:
            return True
            
        # create graph
        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        
        visited = [False] * n
        return self.dfs(start, end, g, visited)


if __name__ == "__main__":
    sol = Solution()

    n = 3
    edges = [[0,1],[1,2],[2,0]]
    start = 0
    end = 2
    print(sol.validPath(n, edges, start, end))

    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    start = 0
    end = 5
    print(sol.validPath(n, edges, start, end))

    n = 1
    edges = []
    start = 0
    end = 0
    print(sol.validPath(n, edges, start, end))

    n = 10
    edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    start = 5
    end = 9
    print(sol.validPath(n, edges, start, end))