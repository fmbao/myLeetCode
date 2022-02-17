
#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        data_len = len(nums)
        jump = 0
        farthest = 0
        end = 0
        for i in range(data_len-1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jump += 1
                end = farthest
        return jump





# @lc code=end

