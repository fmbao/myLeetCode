# @before-stub-for-debug-begin
from python3problem62 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:


    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划
        # dp = [[1] * n] + [ [1]+ [0] * (n-1) for _ in range(m-1)]
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]


        # return dp[-1][-1]
        # 回溯

        def traceBack(m,n):
            if m == 1 and n == 1:
                count += 1
                return
            m -=1
            traceBack(m,n)
            m +=1
            n -=1
            traceBack(m,n)
            n +=1

        if m==0 or n==0:
            return 0
        global count
        count  =0
        traceBack(m,n)

        return count

# @lc code=end

