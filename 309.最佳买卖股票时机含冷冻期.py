
#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if i -2 == -1:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[n-1][0]
# @lc code=end

