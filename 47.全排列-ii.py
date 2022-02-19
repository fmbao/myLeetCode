# @before-stub-for-debug-begin
from python3problem47 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        result = []
        used = [False for _ in range(len(nums))]
        def traceBack(used, nums, single_path):
            if len(nums) == len(single_path):
                result.append(single_path[:]) # 核心点
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i-1] == nums[i] and not used[i-1]: ## 核心点
                        continue
                    used[i] = True
                    single_path.append(nums[i])
                    traceBack(used, nums, single_path)
                    single_path.pop()
                    used[i]=False

        nums.sort()
        traceBack(used, nums, [])
        return result
# @lc code=end

