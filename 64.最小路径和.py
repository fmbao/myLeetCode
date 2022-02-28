# @before-stub-for-debug-begin
from python3problem64 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MAX_INT = 2**31 - 1
        memo = [[-1]* n for _ in range(m)]
        def dp(grid,i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i < 0 or j < 0:
                return MAX_INT

            if memo[i][j] == -1:
                memo[i][j] = min(dp(grid,i-1,j),dp(grid,i,j-1)) + grid[i][j]
            return memo[i][j]

        return dp(grid,m-1,n-1)

# @lc code=end

