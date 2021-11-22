from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, partial, graph, visited, result):
        N = len(graph)
        node = partial[-1]
        for nbr in graph[node]:
            if visited[nbr]:
                continue
            if nbr == N-1:
                result.append(partial + [nbr])
                continue 
            visited[nbr] = True
            partial.append(nbr)
            self.dfs(partial, graph, visited, result)
            partial.pop()
            visited[nbr] = False

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        if N == 0:
            return []
        if N == 1:
            return [[0]]
        
        result = []
        visited = [True] + [False] * (N - 1)
        self.dfs([0], graph, visited, result)
        return result


if __name__ == "__main__":
    sol = Solution()

    graph = [[1,2],[3],[3],[]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[1],[]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[1,2,3],[2],[3],[]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[1,3],[2],[3],[]]
    print(sol.allPathsSourceTarget(graph))
