
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Rotate the head
        分成三个步骤来做
        0.
        1. 找到倒数第k个节点
        2. 将倒数第k个节点，衔接到开头
        """
        if not head  or not head.next or k ==0:
            return head

        fast = head
        slow = head
        countPtr = head
        count = 0
        while countPtr:
            countPtr = countPtr.next
            count += 1
        k = k % count
        if k ==0: # 非常关键，这是应对 k正好等于链表长度的情况
            return head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead


# @lc code=end

