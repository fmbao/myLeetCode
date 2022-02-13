
#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        low,high = 0, len(nums)-1 #
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid +1
                else:
                    high = mid - 1
        return -1

# @lc code=end

