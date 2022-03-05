
#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        direct = [[1,0],[0,1],[-1,0],[0,-1]]
        def traceBack(x,y,idx):
            if board[x][y] != word[idx]:
                return False
            if idx == len(word)-1:
                return True

            board[x][y] = '#'  # 本质上来说也是回溯，三部曲，先认为 已经核定了输入 然后再判断接下来的几个位置是否合适
            # 然后再将输入的位置再输出出来
            for single_direct in direct:
                nx = x + single_direct[0]
                ny = y + single_direct[1]
                if 0 <= nx < row  and 0<= ny < col and traceBack(nx,ny, idx+ 1):
                    return True
            board[x][y] = word[idx]


        for x in range(row):
            for y in range(col):
                if traceBack(x,y,0):
                    return True
        return False

# @lc code=end

