
# @before-stub-for-debug-begin
from python3problem300 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
# @lc code=end

