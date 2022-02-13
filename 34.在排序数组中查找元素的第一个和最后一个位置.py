# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end


# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def findLeftIdx(self,nums, target):
        low,high = 0,len(nums)-1
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] >= target:
                high = mid -1
            else:
                low = mid + 1
        if  nums[low]== target:
            return low
        else:
            return -1

    def findRightIdx(self,nums, target):
        low,high = 0,len(nums)-1
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] <= target:
                low = mid+1
            else:
                high = mid -1
        if nums[high] == target:
            return high
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1,-1]
        leftIdx = self.findLeftIdx(nums, target)
        rightIdx = self.findRightIdx(nums, target)
        return [leftIdx, rightIdx]

# @lc code=end

