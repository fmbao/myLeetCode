# @before-stub-for-debug-begin
from python3problem63 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 这一题太不容易了
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] !=1:
                    if i==j == 0:
                        dp[i][j] = 1
                    else:
                        a = dp[i-1][j] if i!=0 else 0
                        b = dp[i][j-1] if j!=0 else 0

                        dp[i][j] = a + b
        return dp[-1][-1]

# @lc code=end

