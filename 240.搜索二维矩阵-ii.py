# @before-stub-for-debug-begin
from python3problem240 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## 使用二分法 求解

        row_idx = len(matrix) -1
        col_idx = len(matrix[0]) -1

        def binary_search(nums:List[int],target:int):
            start = 0
            end = len(nums) -1 # number
            for i in range(len(nums)):

                mid = (start + end) >> 1
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            return -1
        # if row_idx ==0 or col_idx ==0:return False
        # if target< matrix[0][0] or target< matrix[-1][-1]:
        #     return False
        for i in range(len(matrix)):
            if target< matrix[i][0]:
                break
            if target > matrix[i][len(matrix[i])-1]:
                continue
            col_idx = binary_search(matrix[i],target)
            if col_idx != -1:
                return True
        return False



# @lc code=end

