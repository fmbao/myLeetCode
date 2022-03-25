# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        left = 1
        right =1
        for i in range(len(nums)-1):
            left *= nums[i]
            res.append(left)

        for i in range(len(nums)-1,0,-1):
            right *= nums[i]
            res[i-1] *= right
        return res



# @lc code=end

