# @before-stub-for-debug-begin
from python3problem287 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        root = 0
        while slow!=root:
            slow = nums[slow]
            root = nums[root]
        return root


        # slow = nums[0]         #先走一步
        # fast = nums[nums[0]]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        # root = 0
        # while root != slow:
        #     root = nums[root]
        #     slow = nums[slow]
        # return slow





        # repeatFlag = 0
        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if nums[i] != nums[i+1]:
        #         continue
        #     else:
        #         repeatFlag = nums[i]
        #         break
        # if nums[-1] == nums[-2]:
        #     return nums[-1]
        # return repeatFlag

# @lc code=end

