# @before-stub-for-debug-begin
from python3problem59 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    """需要注意的是，千万不能用
        import numpy as np result_matrix = np.zeros((n,n))
        构建初始化数组，会出错。
        然后就是设置四个边界的时候，需要注意范围，同时range也需要注意一个范围"""


    def generateMatrix(self, n: int) -> List[List[int]]:
        import numpy as np
        # result_matrix = np.zeros((n,n))
        result_matrix = [[0 for _ in range(n)]  for _ in range(n) ]
        left_bound = 0
        right_bound = n-1
        top_bound = 0
        bottom_bound = n-1
        count = 1
        while count <= n*n:
            if top_bound <= bottom_bound:
                for y in range(left_bound,right_bound+1):
                    result_matrix[top_bound][y] = count
                    count += 1
                top_bound += 1

            if left_bound <= right_bound:
                for y in range(top_bound,bottom_bound+1):
                    result_matrix[y][right_bound] = count
                    count += 1
                right_bound -= 1

            if bottom_bound >= top_bound:
                for y in range(right_bound,left_bound-1,-1):
                    result_matrix[bottom_bound][y] = count
                    count += 1
                bottom_bound -= 1

            if left_bound <= right_bound:
                for y in range(bottom_bound,top_bound-1,-1):
                    result_matrix[y][left_bound] = count
                    count += 1
                left_bound += 1


        return result_matrix
# @lc code=end

