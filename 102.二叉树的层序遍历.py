# @before-stub-for-debug-begin
from python3problem102 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        queue = collections.deque() # 注意
        if root == None:
            return []
        queue.append(root)
        result = []
        level = []
        while queue:
            size = len(queue)
            level = [] # 清空
            for _ in range(size):
                element = queue.popleft()
                if element == None:
                  continue
                level.append(element.val)
                queue.append(element.left)
                queue.append(element.right)
            if level:
                result.append(level)
        return result

# @lc code=end

