# @before-stub-for-debug-begin
from python3problem71 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split('/')
        stack = []
        for element in elements:
            if element == ".." :
                if stack:
                    stack.pop() # 将stack 判断和 '..'区分开
            elif element and element != ".":
                stack.append(element)

        return '/' + '/'.join(stack)



# @lc code=end

