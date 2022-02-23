# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_bound = 0
        right_bound = len(matrix[0]) -1
        up_bound = 0
        bottom_bound = len(matrix) -1
        n = len(matrix)
        m = len(matrix[0])

        result = list()
        while len(result) < n*m: # 长度单独设置
            if up_bound <= bottom_bound:
                for first_loop_idx in range(left_bound,right_bound+1):
                    result.append(matrix[up_bound][first_loop_idx])
                up_bound += 1
            if left_bound <= right_bound:
                for second_loop_idx in range(up_bound,bottom_bound+1):
                    result.append(matrix[second_loop_idx][right_bound])
                right_bound -= 1
            if bottom_bound >= up_bound:
                for third_loop_idx in range(right_bound,left_bound-1,-1): # 核心 需要进行减一
                    result.append(matrix[bottom_bound][third_loop_idx])
                bottom_bound -= 1
            if right_bound >= left_bound:
                for forth_loop_idx in range(bottom_bound,up_bound-1,-1):
                    result.append(matrix[forth_loop_idx][left_bound]) # 左右问题需要注意
                left_bound += 1
        return result
# @lc code=end

