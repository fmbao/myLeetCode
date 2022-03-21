
#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        rows = len(matrix)
        cols = len(matrix[0])

        maxSides = 0
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i ==0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1

                maxSides = max(maxSides,dp[i][j])
        return maxSides * maxSides

# @lc code=end

