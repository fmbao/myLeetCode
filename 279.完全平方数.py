
#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        ## 采用动态规划的思想
        dp = [j for j in range(n+1)]
        for i in range(1,n):
            nums = i*i
            if nums > n:
                break
            for j in range(nums, n+1):
                dp[j] = min(dp[j], dp[j-nums]+1)
        return dp[n]





# @lc code=end

