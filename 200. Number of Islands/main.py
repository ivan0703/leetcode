from typing import List

class Solution:
    def bfs(self, grid, x, y, visited):
        M, N = len(grid), len(grid[0])

        visited[x][y] = True
        qu = [[x,y]]
        dir = [[-1,0],[0,1],[1,0],[0,-1]]

        while qu:
            sz = len(qu)
            for i in range(sz):
                elem = qu[0]
                qu.pop(0)
                for d in dir:
                    nx = elem[0] + d[0]
                    ny = elem[1] + d[1]
                    if nx>=0 and nx<M and ny>=0 and ny<N and grid[nx][ny]=="1" and not visited[nx][ny]:
                        qu.append([nx,ny])
                        visited[nx][ny] = True
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        M, N = len(grid), len(grid[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        cnt = 0

        for x in range(M):
            for y in range(N):
                if grid[x][y] == "1" and not visited[x][y]:
                    self.bfs(grid, x, y, visited)
                    cnt += 1

        return cnt

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    
    sol = Solution()
    print(sol.numIslands(grid))

        