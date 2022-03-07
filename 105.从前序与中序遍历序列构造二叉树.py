
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 其实这一题本质就是获取到 root root.right root.left
        # 特殊情况判断
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        midIdx = inorder.index(preorder[0])
        ## 获取到前序遍历中的左子树的序列和右子树的序列，这样才能通过递归构建序列
        preLeftorder = preorder[1:midIdx+1] # 这个地方需要注意，两个序号是相互衔接的
        preRightorder = preorder[midIdx+1:]
        ## 获取到中序遍历中的左子树的序列和右子树的序列，这样才能通过递归构建序列
        inLeftorder = inorder[:midIdx]
        inRightorder = inorder[midIdx+1:]

        root.left =  self.buildTree(preLeftorder, inLeftorder)
        root.right =  self.buildTree(preRightorder, inRightorder)
        return root


# @lc code=end

