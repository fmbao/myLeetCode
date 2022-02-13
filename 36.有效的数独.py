# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 这一题只是判断给定的 数独表格里面是否有重复的数字
        row = [[0]* 10 for _ in range(9)]
        col = [[0]* 10 for _ in range(9)]
        box = [[0]* 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                curNum = int(board[i][j]) - int('0')
                # curNum = ord(board[i][j]) - ord('0')
                if row[i][curNum] !=0 or col[j][curNum] != 0 or box[j//3+(i//3)*3][curNum] != 0:
                    return False
                else:
                    row[i][curNum] = 1
                    col[j][curNum] = 1
                    box[j//3+(i//3)*3][curNum] = 1

        return True




# @lc code=end

