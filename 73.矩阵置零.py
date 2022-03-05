
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = [False] * len(matrix)
        col_flag = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col_flag[j] = True
                    row_flag[i] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if col_flag[j] or row_flag[i]:
                    matrix[i][j] = 0


# @lc code=end

