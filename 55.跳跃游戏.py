# @before-stub-for-debug-begin
from python3problem55 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #这道题通过贪心算法进行求解，其实贪心算法也是动态规划的一种，都是用来求最值
        #同时解释一下贪心算法：贪心算法就是每一步都求取最优的结果
        farthest = 0

        for i in range(len(nums)-1): # 非常关键，这道题目意思是无法达到n-1的位置
            farthest = max(farthest,nums[i] + i)
            if farthest <= i: # 这个等于号很关键，代表正好在这个位置无法跳过去
                return False
        return farthest >= (len(nums) - 1)
# @lc code=end

