# @before-stub-for-debug-begin
from python3problem128 import *
from typing import *
# @before-stub-for-debug-end



#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0 :
            return 0

        nums = set(nums)
        nums = list(nums)
        nums.sort()
        ## 采用双指针法进行处理
        start = 0
        end = 0
        count = 0
        while end < len(nums)-1:
            if nums[end+1] - nums[end] ==1:
                end +=1
            else:
                count = max(count, end-start+1)
                start = (end+1)
                end += 1
            # count = end - start
        count = max(count, end-start+1)
        return count
# @lc code=end

