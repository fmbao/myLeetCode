
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 这一题主要是应用的递归，想法就是要保障左子树和右子树所有内容都
        # 都需要 大小的保障所以需要设置三个核心参数
        def isValidBSTCore(root, min, max):
            if root == None:
                return True
            if min!=None and root.val <= min.val: return False # 核心
            if max!=None and root.val >= max.val: return False # 核心
            return isValidBSTCore(root.left, min , root) and isValidBSTCore(root.right, root ,max)

        return isValidBSTCore(root, None ,None)






# @lc code=end

