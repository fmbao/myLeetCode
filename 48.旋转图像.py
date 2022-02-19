
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 我主要参考的这个 https://leetcode-cn.com/problems/rotate-image/solution/48-xuan-zhuan-tu-xiang-fu-zhu-ju-zhen-yu-jobi/
        n= len(matrix)

        for i in range(n//2):
            for j in range((n+1)//2): # 核心要点
                #基本规律  中间相加为 n-1 两边相等 上一行后面的和下一行前面的相等
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]

                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp



# @lc code=end

