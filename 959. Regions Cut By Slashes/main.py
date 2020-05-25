from typing import List

class Solution:
    def dfs(self, i, j, dir, grid, edges):
        N = len(grid)
        if i<0 or i>=N or j<0 or j>=N or edges[i][j][dir]:
            return
        
        # update edges
        if grid[i][j]=='/':
            if dir == 0 or dir == 3:
                edges[i][j][0] = edges[i][j][3] = True
                self.dfs(i,j-1,1,grid,edges)
                self.dfs(i-1,j,2,grid,edges)
            else:
                edges[i][j][1] = edges[i][j][2] = True
                self.dfs(i+1,j,0,grid,edges)
                self.dfs(i,j+1,3,grid,edges)
        elif grid[i][j] == '\\':
            if dir == 0 or dir == 1:
                edges[i][j][0] = edges[i][j][1] = True
                self.dfs(i,j+1,3,grid,edges)
                self.dfs(i-1,j,2,grid,edges)
            else:
                edges[i][j][2] = edges[i][j][3] = True
                self.dfs(i,j-1,1,grid,edges)
                self.dfs(i+1,j,0,grid,edges)
        else:
            edges[i][j] = [True] * 4
            self.dfs(i-1,j,2,grid,edges)
            self.dfs(i+1,j,0,grid,edges)
            self.dfs(i,j-1,1,grid,edges)
            self.dfs(i,j+1,3,grid,edges)

    def regionsBySlashes(self, grid: List[str]) -> int:
        if len(grid)==0:
            return 0

        N = len(grid)
        edges = [[[False]*4 for _ in range(N)] for _ in range(N)]
        
        region = 0
        for i in range(N):
            for j in range(N):
                for d in range(4):
                    if not edges[i][j][d]:
                        self.dfs(i,j,d,grid,edges)
                        region += 1
        return region

if __name__ == "__main__":
    sol = Solution()
    print(sol.regionsBySlashes([" /","/ "]))
    print(sol.regionsBySlashes([" /","  "]))
    print(sol.regionsBySlashes(["\\/","/\\"]))
    print(sol.regionsBySlashes(["/\\","\\/"]))
    print(sol.regionsBySlashes(["//","/ "]))