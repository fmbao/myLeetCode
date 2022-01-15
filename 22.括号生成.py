'''
Author: your name
Date: 2022-01-15 19:31:16
LastEditTime: 2022-01-16 00:41:11
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/22.括号生成.py
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        curStr = ""
        def dfs(curStr,left, right):
            # 回溯-> 深度优先搜索
            # curStr: 从根节点到叶子节点的路径字符串
            # left: 左括号还可以使用的个数
            # right: 右括号还可以使用的数量
            if right == 0 and left == 0:
                res.append(curStr)
            if right < left:
                return

            if left > 0:
                dfs(curStr + "(", left-1, right)
            if right > 0:
                dfs(curStr + ")", left, right - 1)
        dfs(curStr, n, n)
        return res


# @lc code=end

