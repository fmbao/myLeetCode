'''
Author: baochenchen
Date: 2022-01-15 17:35:57
LastEditTime: 2022-01-15 18:46:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode/19.删除链表的倒数第-n-个结点.py
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """.vscode/
        1. 设置两个指针，先让快指针走n个单位
        2. 再让两个指针同步开始走
        3. 当快指针走到链表的尽头，就表示需要让慢指针删除当前节点
        4. 然后慢节点再后退至头结点就可以了

        """
        finalNode = ListNode(0)
        finalNode.next = head
        fast = finalNode

        slow = finalNode
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return finalNode.next

# @lc code=end

