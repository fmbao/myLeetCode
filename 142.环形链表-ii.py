# @before-stub-for-debug-begin
from python3problem142 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        142 环形链表2.py
        基本的思路就是用双指针进行遍历
        需要注意的是，两个地方
        一个是链表不是循环链表的判断条件：需要fast 和 fast.next 有一个为空
        另一个条件是 找环所在的位置  从头起一个指针同时和slow开始遍历  然后两个指针相遇的位置就是环所在的位置
        """


        slow = head
        fast = head
        count = 0
        while True:
            if not (fast and fast.next): return
            slow = slow.next
            fast = fast.next.next
            if fast == slow :
                break
        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next

        return cur



# @lc code=end

