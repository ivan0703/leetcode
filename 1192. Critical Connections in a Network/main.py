from typing import List
import math

class Solution:

    def dfs(self, root, parent, graph, layer, group, start):
        layer[root] = start
        group[root] = start
        start += 1

        # loop through the neighbors of root
        for node in graph[root]:
            if node == parent:
                continue
            if layer[node] == -1:
                self.dfs(node, root, graph, layer, group, start)
                group[root] = min(group[root], group[node])
            else:
                group[root] = min(group[root], layer[node])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        
        # construct graph
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        
        layer = [-1] * n
        group = [math.inf] * n
        self.dfs(0, -1, graph, layer, group, 0)
        
        res = []
        for c in connections:
            if group[c[0]] > layer[c[1]] or layer[c[0]] < group[c[1]]:
                res.append(c) 
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))