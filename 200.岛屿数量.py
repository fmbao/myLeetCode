class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            if i >=m or i < 0 or j < 0 or j >=n:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid,i,j+1)
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1':
                    res +=1
                    dfs(grid,i,j)
        return res

