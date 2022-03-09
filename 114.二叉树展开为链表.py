# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        stack = []  # 需要注意的是  这个是stack  需要注意数据进出的顺序
        temp = None

        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node is not None:
                stack.append(cur_node.right)
                stack.append(cur_node.left)
                if temp is not None:
                    temp.right = cur_node
                cur_node.left = None
                temp = cur_node


# @lc code=end

