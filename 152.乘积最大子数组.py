# @before-stub-for-debug-begin
from python3problem152 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## 用回溯算法进行处理
        min_num = 1
        max_num = 1
        res = -2**10
        for single_data in nums:
            if single_data < 0:
                tmp = max_num
                max_num = min_num
                min_num = tmp
            min_num = min(min_num * single_data, single_data)
            max_num = max(max_num * single_data, single_data)
            res = max(max_num, res)

        return res



# @lc code=end

