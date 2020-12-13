class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        visited = {(0,0)}
        dir = [
            [1,2], [1,-2], [2,1], [2,-1],
            [-1,2],[-1,-2],[-2,1],[-2,-1]
        ]

        ret, qu = 0, [[0,0]]
        while qu:
            sz = len(qu)
            for _ in range(sz):
                elem = qu[0]
                qu.pop(0)
                for d in dir:
                    dx = elem[0] + d[0]
                    dy = elem[1] + d[1]
                    if dx == x and dy == y:
                        return ret + 1
                    if (dx,dy) not in visited:
                        visited.add((dx,dy))
                        qu.append([dx,dy])
            if qu:
                ret += 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.minKnightMoves(2,1))
    print(sol.minKnightMoves(5,5))