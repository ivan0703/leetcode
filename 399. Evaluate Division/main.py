from typing import List, Dict
from collections import defaultdict

class Solution:
    def bfs(self, qry, graph, res):
        if qry[0] not in graph or qry[1] not in graph:
            return -1

        if qry[0] == qry[1]:
            return 1
        if (qry[0],qry[1]) in res:
            return res[(qry[0],qry[1])]
        
        qu = [(qry[0],1)]
        while qu:
            sz = len(qu)
            for i in range(sz):
                d1, v = qu.pop(0)
                for d2 in graph[d1]:
                    if (qry[0],d2) not in res:
                        m = v * graph[d1][d2]
                        qu.append((d2, m))
                        res[(qry[0],d2)] = m
        
        if (qry[0],qry[1]) in res:
            return res[(qry[0],qry[1])]
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # make graph
        g = defaultdict(dict)
        for eq, v in zip(equations, values):
            g[eq[0]][eq[1]] = v
            g[eq[1]][eq[0]] = 1 / v

        res = {}
        result = []
        for qry in queries:
            result.append(self.bfs(qry, g, res))
        return result
        

if __name__ == "__main__":
    sol = Solution()

    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)

    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)

    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)

    equations = [["a","b"],["c","d"]]
    values = [1.0,1.0]
    queries = [["a","c"],["b","d"],["b","a"],["d","c"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)

    equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
    values = [3.0,0.5,3.4,5.6]
    queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)

    equations = [["a","b"],["a","c"],["a","d"],["a","e"],["a","f"],["a","g"],["a","h"],["a","i"],["a","j"],["a","k"],["a","l"],["a","aa"],["a","aaa"],["a","aaaa"],["a","aaaaa"],["a","bb"],["a","bbb"],["a","ff"]]
    values = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,1.0,1.0,1.0,1.0,1.0,3.0,5.0]
    queries = [["d","f"],["e","g"],["e","k"],["h","a"],["aaa","k"],["aaa","i"],["aa","e"],["aaa","aa"],["aaa","ff"],["bbb","bb"],["bb","h"],["bb","i"],["bb","k"],["aaa","k"],["k","l"],["x","k"],["l","ll"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)