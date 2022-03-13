# @before-stub-for-debug-begin
from python3problem148 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## 思路，将 所有元素取出排序  然后从hash表中对应产生新的链表
        if head is None:
            return head
        all_vals = []
        cur = head
        while cur is not None:
            all_vals.append(cur.val)
            cur = cur.next
        all_vals.sort()
        count = 0
        new_node_list = ListNode(all_vals[count])
        cur = new_node_list
        while count < len(all_vals)-1:
            count +=1
            new_node = ListNode(all_vals[count])
            cur.next = new_node
            cur = new_node
        return new_node_list
# @lc code=end

