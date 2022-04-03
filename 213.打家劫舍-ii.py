# @before-stub-for-debug-begin
from python3problem213 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        ## 这类问题 存在已经非常简化的写法
        def dp(nums, start: int, end: int):
            n = len(nums)
            dp_i_1 = 0
            dp_i_2 = 0
            for i in range(end,start-1,-1):
                dp_i = max(dp_i_1, dp_i_2 + nums[i])
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i
        if len(nums)==1:
            return nums[0]
        return  max(dp(nums,0,len(nums)-2),dp(nums,1,len(nums)-1))


# @lc code=end

