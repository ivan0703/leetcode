#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    void bfs(vector<vector<char>> &grid, int x, int y, vector<vector<bool>> &visited) {
        int M = grid.size();
        int N = grid[0].size();

        visited[x][y] = true;

        queue<pair<int,int>> qu;
        int dir_x[4] = {-1, 0, 1, 0};
        int dir_y[4] = { 0, 1, 0,-1};
        qu.push({x,y});

        while(!qu.empty()) {
            int sz = qu.size();
            for(int i=0; i<sz; i++) {
                pair<int,int> pt = qu.front();
                qu.pop();

                // traverse its eight neighbors
                for(int k=0; k<4; k++) {
                    int dx = pt.first + dir_x[k];
                    int dy = pt.second + dir_y[k];
                    if(dx>=0 && dx<M && dy>=0 && dy<N && grid[dx][dy]=='1' && !visited[dx][dy]) {
                        qu.push({dx, dy});
                        visited[dx][dy] = true;
                    }
                }
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        if(grid.size()==0 || grid[0].size()==0)
            return 0;

        int M = grid.size();
        int N = grid[0].size();
        vector<vector<bool>> visited(M, vector<bool>(N,false));

        int ans = 0;
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]=='1' && !visited[i][j]) {
                    bfs(grid,i,j,visited);
                    ans++;
                }
            }
        }
        return ans;
    }
};

int main()
{
    vector<vector<char>> grid1 = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'},
    };

    vector<vector<char>> grid2 = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'},
    };

    Solution sol;
    cout<<sol.numIslands(grid1)<<endl;
    cout<<sol.numIslands(grid2)<<endl;

    return 0;
}