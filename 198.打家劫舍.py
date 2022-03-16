
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        ## 贪心算法
        if len(nums) <2:
            return nums[0] if len(nums) == 1 else 0
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]
        res[1] = nums[1]
        for i in range(2,len(nums),1):
            res[i] = max(res[i-2] + nums[i], res[i-1] - nums[i-1] + nums[i])

        return max(res[-1], res[-2])

# @lc code=end

