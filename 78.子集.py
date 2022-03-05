# @before-stub-for-debug-begin
from python3problem78 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        def trackBack(startId, path):
            result.append(path[:])
            for i in range(startId, n):
                path.append(nums[i])
                trackBack(i + 1 , path) # 核心关键
                path.pop()
        trackBack(0, path)
        return result
# @lc code=end

