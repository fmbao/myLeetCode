
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
        # if head is None:
        #     return head
        # all_vals = []
        # cur = head
        # while cur is not None:
        #     all_vals.append(cur.val)
        #     cur = cur.next
        # all_vals.sort()
        # count = 0
        # new_node_list = ListNode(all_vals[count])
        # cur = new_node_list
        # while count < len(all_vals)-1:
        #     count +=1
        #     new_node = ListNode(all_vals[count])
        #     cur.next = new_node
        #     cur = new_node
        # return new_node_list
        ## 另外一种方法就是归并排序，能够在比较短的时间复杂度以及空间复杂度上完成指定的计算
        if not head or not head.next: return head
        left_end = self.findMidNode(head)
        mid = left_end.next
        left_end.next = None
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge(left, right)

        if not head  or not  head.next : return head

        mid_left_node = self.findMidNode(head)
        ## 关键将左右两边切分开

        mid = mid_left_node.next
        mid_left_node.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)

    def findMidNode(self, head):
        ## 注意边界条件，如果其中有一个不存在，就返回head
        if head is None or head.next is None:return head
        fast,slow = head.next,head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, left,right):
        res = ListNode()
        cur = res

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        return res.next

# @lc code=end

