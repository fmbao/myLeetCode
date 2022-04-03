
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## 主要的实现方式是动态规划
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return  -1 if dp[-1] == amount + 1 else dp[-1]
# @lc code=end

